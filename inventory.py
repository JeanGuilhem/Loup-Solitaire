"""
Inventaire et état du Loup Solitaire.

Tout l'état de la partie vit dans st.session_state (cf. DEFAULT_STATE) sous forme de listes
et d'entiers simples, ce qui le rend directement sérialisable dans le cookie de sauvegarde.

Cycle de vie d'une page de paragraphe :
    check_inventory(current_page_number=N)   # en haut de page
    ...                                      # texte, choix, combats, objets
    end_page()                               # dernière ligne de la page
"""
import functools
import json
import unicodedata

import streamlit as st

from game_stats import record_page
from save import delete_save, page_path, save_game
from utils import ls_death
from variable import BOOKS, ITEMS, KAI, MAX_BACKPACK, MAX_PURSE, MAX_WEAPONS

BACKPACK_ITEM = "SAC À DOS"
MAX_VISIBILITY_FLAGS = 10

DEFAULT_STATE = {
    "hability": 0,
    "endurance": 0,
    "total_endurance": 0,
    "purse": 0,
    "weapons": [],
    "backpack": [],
    "has_backpack": True,
    "special": [],
    "kai": [],
    "weapon_mastery": [],
    "current_page_number": 0,
    "last_page_number": 0,
    "book": 1,  # tome en cours
    "completed_books": [],
    "provenance": {},  # objet -> d'où il vient (fiche de l'écran d'équipement)
    "done_fighting": False,
    "flee": False,
    "page_has_fight": False,
}


# --------------------------------------------------------------------------------------
# Noms : les pages générées écrivent "Repas", "REPAS", "Clé d'Or", "Sixième Sens"...
# --------------------------------------------------------------------------------------
def _normalize(text: str) -> str:
    text = str(text).replace("’", "'").replace(",", " ").strip().upper()
    text = "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    )
    return " ".join(text.split())


def _strip_article(text: str) -> str:
    for article in ("LE ", "LA ", "LES ", "L'"):
        if text.startswith(article):
            return text[len(article):]
    return text


_ITEM_INDEX = {_normalize(name): name for name in ITEMS}
_KAI_INDEX = {_strip_article(_normalize(name)): name for name in KAI}


def canonical_item(name: str) -> str:
    """Nom canonique de l'objet dans le catalogue (ou le nom en majuscules s'il est inconnu)."""
    normalized = _normalize(name)
    if normalized == _normalize(BACKPACK_ITEM):
        return BACKPACK_ITEM
    if normalized in _ITEM_INDEX:
        return _ITEM_INDEX[normalized]
    # pluriels simples : "Repas" est invariable mais "Torches", "Lances"...
    if normalized.endswith("S") and normalized[:-1] in _ITEM_INDEX:
        return _ITEM_INDEX[normalized[:-1]]
    return str(name).strip().upper()


def item_info(name: str) -> dict:
    """Fiche catalogue d'un objet. Un objet inconnu va dans le Sac à Dos (règle du livre)."""
    return ITEMS.get(canonical_item(name), {"type": "backpack", "description": ""})


def canonical_kai(name: str):
    return _KAI_INDEX.get(_strip_article(_normalize(name)))


# --------------------------------------------------------------------------------------
# État
# --------------------------------------------------------------------------------------
def init_state() -> None:
    """Crée les clés manquantes de st.session_state avec leurs valeurs par défaut."""
    for key, value in DEFAULT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = type(value)(value) if isinstance(value, (list, dict)) else value
    for i in range(1, MAX_VISIBILITY_FLAGS + 1):
        if f"visibility_{i}" not in st.session_state:
            st.session_state[f"visibility_{i}"] = False


def reset_state() -> None:
    """Nouvelle partie : efface tout l'état de jeu (et la sauvegarde)."""
    for key in list(st.session_state.keys()):
        if key != "cookie_manager":
            del st.session_state[key]
    init_state()
    delete_save()


def _reset_page_flags() -> None:
    """Remet à zéro les drapeaux propres à une page (objets ramassés, combats faits)."""
    for key in list(st.session_state.keys()):
        if key.startswith("visibility_"):
            st.session_state[key] = False
        elif key.startswith("done_fighting"):
            st.session_state[key] = False
        elif key.startswith(("combat_", "hazard_")):
            del st.session_state[key]
    st.session_state.pop("artifact_choice", None)  # objet examiné dans l'écran d'équipement
    st.session_state.flee = False
    st.session_state.page_has_fight = False
    st.session_state.streamed_texts = []


def is_new_page() -> bool:
    """True au premier rendu d'une page, False lors des reruns (clic sur un bouton...)."""
    return st.session_state.last_page_number != st.session_state.current_page_number


def illustrations_dir(book: int) -> str:
    return f"static/illustrations/tome{book}"


@functools.lru_cache(maxsize=None)
def _illustrations_index(book: int) -> dict:
    """{numéro de paragraphe: [illustrations]} d'après static/illustrations/tome<N>/illustrations.json."""
    try:
        with open(f"{illustrations_dir(book)}/illustrations.json", encoding="utf-8") as index_file:
            entries = json.load(index_file)
    except (OSError, ValueError):
        return {}
    index = {}
    for entry in entries:
        index.setdefault(entry["paragraph"], []).append(entry)
    return index


def show_illustrations() -> None:
    """Affiche les illustrations du paragraphe en cours, comme dans le livre : après les choix."""
    book = st.session_state.book
    for entry in _illustrations_index(book).get(st.session_state.current_page_number, []):
        st.image(f"{illustrations_dir(book)}/{entry['file']}", caption=entry.get("caption"))


@functools.lru_cache(maxsize=None)
def _page_has_fight(book: int, page_number: int) -> bool:
    """Un paragraphe contient un combat si sa page appelle combat()."""
    try:
        with open(page_path(page_number, book), encoding="utf-8") as page_file:
            return "combat(" in page_file.read()
    except OSError:
        return False


def check_inventory(is_fighting: bool = False, current_page_number: int = 0, book: int = 1) -> None:
    """
    À appeler en haut de chaque page de paragraphe.
    is_fighting: conservé pour compatibilité, les combats sont détectés automatiquement.
    book: tome de la page (les pages du tome 1 ne le précisent pas).
    """
    init_state()
    st.session_state.book = book
    st.session_state.current_page_number = current_page_number
    st.set_page_config(page_title=f"Paragraphe {current_page_number}", page_icon="📜")
    st.header(f"📜 Paragraphe {current_page_number}", divider="gray")
    if is_new_page():
        _reset_page_flags()
        st.session_state.page_has_fight = is_fighting or _page_has_fight(book, current_page_number)
        _apply_healing()


def _apply_healing() -> None:
    """Guérison : +1 ENDURANCE par paragraphe traversé sans combat, sous le total initial."""
    if (
        not st.session_state.page_has_fight
        and has_kai("La Guérison")
        and st.session_state.endurance < st.session_state.total_endurance
    ):
        st.session_state.endurance += 1
        st.toast(
            f"**Guérison : +1 ENDURANCE** "
            f"({st.session_state.endurance}/{st.session_state.total_endurance})",
            icon="🌿",
        )


def end_page() -> None:
    """
    À appeler en dernière ligne de chaque page de paragraphe :
    vérifie les limites et la mort, puis sauvegarde.
    """
    st.session_state.endurance = min(
        st.session_state.endurance, st.session_state.total_endurance
    )
    if st.session_state.purse > MAX_PURSE:
        st.info(
            f"Votre bourse ne peut contenir qu'un maximum de {MAX_PURSE} Couronnes, "
            "vous abandonnez le surplus."
        )
        st.session_state.purse = MAX_PURSE

    if st.session_state.endurance <= 0:
        ls_death()

    if is_new_page():
        book = st.session_state.book
        if st.session_state.current_page_number == BOOKS[book]["final_page"]:
            if book not in st.session_state.completed_books:
                st.session_state.completed_books.append(book)
        record_page()
    st.session_state.last_page_number = st.session_state.current_page_number
    save_game()


# --------------------------------------------------------------------------------------
# Disciplines Kaï
# --------------------------------------------------------------------------------------
def has_kai(name: str) -> bool:
    """has_kai("Le Sixième Sens"), has_kai("Sixième Sens") et has_kai("sixieme sens") sont équivalents."""
    discipline = canonical_kai(name)
    return discipline is not None and discipline in st.session_state.kai


# --------------------------------------------------------------------------------------
# Objets
# --------------------------------------------------------------------------------------
def has_item(name: str) -> bool:
    return count_item(name) > 0


def count_item(name: str) -> int:
    item = canonical_item(name)
    return (
        st.session_state.weapons.count(item)
        + st.session_state.backpack.count(item)
        + st.session_state.special.count(item)
    )


def has_weapon() -> bool:
    return len(st.session_state.weapons) > 0


def _record_origin(item: str, origin: str = None) -> None:
    """Note d'où vient un objet (fiche de l'écran d'équipement) : par défaut le tome et le paragraphe."""
    book = st.session_state.get("book", 1)
    page = st.session_state.get("current_page_number", 0)
    default = f"Tome {book}, paragraphe {page}." if page else f"Tome {book}."
    st.session_state.setdefault("provenance", {})[item] = origin or default


def add_to_inventory(name: str, quantity: int = 1, origin: str = None) -> bool:
    """
    Ajoute un objet là où il doit aller (Armes, Sac à Dos ou Objets Spéciaux).
    Renvoie False (et affiche pourquoi) si la place manque : l'objet n'est alors pas pris.
    origin : provenance affichée dans la fiche de l'objet (par défaut le tome et le paragraphe en cours).
    """
    item = canonical_item(name)
    info = item_info(item)

    if item == BACKPACK_ITEM:
        if st.session_state.has_backpack:
            st.warning("Vous avez déjà un Sac à Dos.")
            return False
        st.session_state.has_backpack = True
        _record_origin(item, origin)
        return True

    for _ in range(quantity):
        if info["type"] == "weapon":
            if len(st.session_state.weapons) >= MAX_WEAPONS:
                st.error(
                    f"Vous ne pouvez porter que {MAX_WEAPONS} armes à la fois. "
                    "Jetez-en une depuis l'onglet Inventaire pour prendre celle-ci."
                )
                return False
            st.session_state.weapons.append(item)

        elif info["type"] == "special":
            st.session_state.special.append(item)
            bonus = info.get("endurance_bonus", 0)
            st.session_state.total_endurance += bonus
            st.session_state.endurance += bonus

        else:
            if not st.session_state.has_backpack:
                st.error("Vous n'avez plus de Sac à Dos pour ranger cet objet.")
                return False
            if len(st.session_state.backpack) >= MAX_BACKPACK:
                st.error(
                    f"Votre Sac à Dos ne peut contenir que {MAX_BACKPACK} objets. "
                    "Jetez un objet depuis l'onglet Inventaire pour prendre celui-ci."
                )
                return False
            st.session_state.backpack.append(item)

    _record_origin(item, origin)
    return True


def remove_from_inventory(name: str, quantity: int = 1) -> bool:
    """Retire un objet (arme, Sac à Dos ou Objet Spécial). Renvoie False s'il n'était pas possédé."""
    item = canonical_item(name)
    removed = False
    for _ in range(quantity):
        for container in ("weapons", "backpack", "special"):
            if item in st.session_state[container]:
                st.session_state[container].remove(item)
                if container == "special":
                    bonus = item_info(item).get("endurance_bonus", 0)
                    st.session_state.total_endurance -= bonus
                    st.session_state.endurance = min(
                        st.session_state.endurance, st.session_state.total_endurance
                    )
                removed = True
                break
    return removed


def lose_all_weapons() -> None:
    st.session_state.weapons = []


def lose_backpack() -> None:
    """Le Sac à Dos et tout son contenu sont perdus (il faudra en retrouver un)."""
    st.session_state.backpack = []
    st.session_state.has_backpack = False


def empty_backpack() -> None:
    """Le contenu du Sac à Dos est perdu, mais pas le sac lui-même."""
    st.session_state.backpack = []


def lose_gold() -> None:
    """« Il ne vous reste plus une seule Pièce d'Or »."""
    st.session_state.purse = 0


def lose_special_items() -> None:
    """Tous les Objets Spéciaux sont perdus (avec les bonus d'ENDURANCE qu'ils donnaient)."""
    for item in list(st.session_state.special):
        remove_from_inventory(item)


def lose_everything() -> None:
    """« On vous a tout volé : Or, Sac à Dos, Armes, ainsi que tous vos Objets Spéciaux »."""
    lose_gold()
    lose_backpack()
    lose_all_weapons()
    lose_special_items()


def choose_item_to_lose(
    candidates: list, key: str = "lose", label: str = "Choisissez l'objet que vous perdez :"
) -> bool:
    """
    Le joueur choisit l'objet qu'il perd parmi `candidates` (vol, arme brisée...), une seule fois
    par visite de la page. S'il n'y a qu'un candidat, il est perdu d'office.
    Renvoie True une fois la perte réglée (ou s'il n'y avait rien à perdre), False tant que le joueur
    n'a pas choisi : la page peut alors attendre avant d'afficher la suite.
    """
    flag = f"visibility_{key}"
    lost = st.session_state.get(flag)
    if lost:
        st.write(f"*Vous avez perdu : {lost}.*")
        return True
    if not candidates:
        return True
    if len(candidates) == 1:
        remove_from_inventory(candidates[0])
        st.session_state[flag] = candidates[0]
        st.write(f"*Vous avez perdu : {candidates[0]}.*")
        return True

    choice = st.selectbox(label, candidates, key=f"{key}_select")
    clicked = st.button("Confirmer", key=f"{key}_confirm")
    if clicked and not st.session_state.get(flag):
        remove_from_inventory(choice)
        st.session_state[flag] = choice
        st.rerun()
    return False


def has_room_for(name: str, quantity: int = 1) -> bool:
    """True si l'objet peut être rangé (2 armes, 8 objets dans le Sac à Dos, Sac à Dos possédé)."""
    item = canonical_item(name)
    kind = item_info(item)["type"]
    if item == BACKPACK_ITEM:
        return not st.session_state.has_backpack
    if kind == "weapon":
        return len(st.session_state.weapons) + quantity <= MAX_WEAPONS
    if kind == "backpack":
        return st.session_state.has_backpack and len(st.session_state.backpack) + quantity <= MAX_BACKPACK
    return True


def choose_gifts(options: dict, count: int, key: str = "gifts", label: str = None) -> bool:
    """
    « Choisissez N objets dans la liste suivante » : une seule fois par visite de la page.
    options : {libellé: (NOM, quantité)}, NOM = None pour des Couronnes.
        choose_gifts({"Glaive": ("GLAIVE", 1), "3 Repas": ("REPAS", 3), "12 Pièces d'Or": (None, 12)}, 1)
    Renvoie True une fois le choix fait.
    """
    flag = f"visibility_{key}"
    if st.session_state.get(flag):
        st.write("*Vous avez choisi : " + ", ".join(st.session_state[flag]) + ".*")
        return True
    chosen = st.multiselect(
        label or f"Choisissez {count} objet(s)", list(options), max_selections=count, key=f"{key}_select"
    )
    missing = [
        choice for choice in chosen
        if options[choice][0] is not None and not has_room_for(*options[choice])
    ]
    if missing:
        st.warning(
            "Pas assez de place pour : " + ", ".join(missing)
            + ". Jetez un objet depuis l'onglet Inventaire ou faites un autre choix."
        )
    if st.button("Prendre", key=f"{key}_confirm", disabled=len(chosen) != count or bool(missing)):
        if not st.session_state.get(flag):
            for choice in chosen:
                name, quantity = options[choice]
                if name is None:
                    add_gold(quantity)
                else:
                    add_to_inventory(name, quantity=quantity)
            st.session_state[flag] = chosen
            st.rerun()
    return False


def use_item(name: str) -> bool:
    """Utilise un objet consommable hors combat (Potion, Laumspur...)."""
    item = canonical_item(name)
    heal = item_info(item).get("heal", 0)
    if not heal or not has_item(item):
        return False
    remove_from_inventory(item)
    change_endurance(heal)
    return True


def pickup_button(name: str, key: str, label: str = None) -> None:
    """
    Bouton « Prendre » pour un objet trouvé : il n'ajoute l'objet qu'une fois par visite de la page,
    et reste cliquable si l'ajout échoue (Sac à Dos plein, déjà 2 armes...).
    Plusieurs boutons partageant la même `key` forment un choix exclusif (« l'un ou l'autre »).
    """
    flag = f"visibility_{key}"
    taken = st.session_state.get(flag, False)
    clicked = st.button(label or f"Prendre : {name}", key=f"pickup_{key}_{name}", disabled=taken)
    # un double-clic rapide arrive avant que le bouton soit grisé : on revérifie le drapeau
    if clicked and not st.session_state.get(flag, False):
        if add_to_inventory(name):
            st.session_state[flag] = True
            st.rerun()


def buy_button(name: str, price: int, key: str, label: str = None, quantity: int = 1) -> None:
    """
    Bouton « Acheter » d'une boutique : paie `price` Couronnes et ajoute l'objet, une seule fois
    par visite de la page. Grisé si la bourse ne suffit pas ; rien n'est payé si la place manque.
    """
    flag = f"visibility_buy_{key}"
    bought = st.session_state.get(flag, False)
    clicked = st.button(
        label or f"Acheter : {name} ({price} Couronnes)",
        key=f"buy_{key}",
        disabled=bought or st.session_state.purse < price,
    )
    if clicked and not st.session_state.get(flag, False):
        if add_to_inventory(name, quantity=quantity) and spend_gold(price):
            st.session_state[flag] = True
            st.toast(f"**{name}** acheté pour {price} Couronne(s)", icon="🛒")
            st.rerun()


def sell_button(name: str, price: int, key: str, label: str = None) -> None:
    """Bouton « Vendre » : retire l'objet possédé et rapporte `price` Couronnes (une fois par visite)."""
    flag = f"visibility_sell_{key}"
    sold = st.session_state.get(flag, False)
    clicked = st.button(
        label or f"Vendre : {name} ({price} Couronnes)",
        key=f"sell_{key}",
        disabled=sold or not has_item(name),
    )
    if clicked and not st.session_state.get(flag, False) and remove_from_inventory(name):
        st.session_state[flag] = True
        add_gold(price)
        st.toast(f"**{name}** vendu pour {price} Couronne(s)", icon="💰")
        st.rerun()


def pickup_gold(amount: int, key: str = "gold") -> None:
    """
    Bouton « Prendre X Couronnes » (une seule fois par visite de la page). Une fois l'or pris,
    affiche la bourse avec le gain, comme l'ENDURANCE en combat, et un pop-up.
    """
    flag = f"visibility_{key}"  # False tant que l'or n'est pas pris, puis le montant réellement gagné
    taken = st.session_state.get(flag, False) is not False
    clicked = st.button(f"Prendre {amount} Couronnes", key=f"pickup_{key}", disabled=taken)
    if clicked and not taken:
        st.session_state[flag] = add_gold(amount, notify=False)
        st.session_state[f"{flag}_toast"] = True
        st.rerun()
    if taken:
        _show_gold_gain(flag, amount)


def receive_gold(amount: int, key: str = "gold_received") -> None:
    """
    Or donné d'office par le texte (récompense, bourse trouvée...) : ajouté une seule fois par
    visite de la page, avec le même affichage que pickup_gold.
    """
    flag = f"visibility_{key}"
    if st.session_state.get(flag, False) is False:
        st.session_state[flag] = add_gold(amount, notify=False)
        st.session_state[f"{flag}_toast"] = True
    _show_gold_gain(flag, amount)


def _show_gold_gain(flag: str, amount: int) -> None:
    """Bourse avec le gain en delta (reste affichée pendant la visite) et pop-up la première fois."""
    gained = st.session_state[flag]
    st.metric(
        label="Couronnes",
        value=f"{st.session_state.purse}/{MAX_PURSE}",
        delta=f"+{gained}" if gained else None,
    )
    if gained < amount:
        st.caption(f"Votre bourse est pleine : vous laissez {amount - gained} Couronne(s) sur place.")
    if st.session_state.get(f"{flag}_toast"):
        st.toast(f"**+{gained} Couronne(s)** ({st.session_state.purse}/{MAX_PURSE})", icon="💰")
        st.session_state[f"{flag}_toast"] = False


# --------------------------------------------------------------------------------------
# Couronnes et ENDURANCE
# --------------------------------------------------------------------------------------
def add_gold(amount: int, notify: bool = True) -> int:
    """Ajoute des Couronnes dans la limite de la bourse. Renvoie le montant réellement ajouté."""
    added = max(0, min(amount, MAX_PURSE - st.session_state.purse))
    st.session_state.purse += added
    if notify and added < amount:
        st.info(
            f"Votre bourse ne peut contenir que {MAX_PURSE} Couronnes : "
            f"vous laissez {amount - added} Couronnes."
        )
    return added


def spend_gold(amount: int) -> bool:
    """Paie `amount` Couronnes. Renvoie False (sans rien retirer) si la bourse ne suffit pas."""
    if st.session_state.purse < amount:
        return False
    st.session_state.purse -= amount
    return True


def change_endurance(delta: int) -> int:
    """Modifie l'ENDURANCE (sans dépasser le total) et gère la mort. Renvoie la nouvelle valeur."""
    st.session_state.endurance = min(
        st.session_state.endurance + delta, st.session_state.total_endurance
    )
    if st.session_state.endurance <= 0:
        st.session_state.endurance = 0
        ls_death()
    return st.session_state.endurance


# --------------------------------------------------------------------------------------
# Affichage (onglet Inventaire)
# --------------------------------------------------------------------------------------
def display_inventory() -> None:
    from artifacts import render_equipment

    render_equipment(
        {key: st.session_state[key] for key in ("weapons", "special", "backpack", "has_backpack", "purse")},
        st.session_state.get("provenance", {}),
    )
    st.divider()
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Couronnes", value=f"{st.session_state.purse}/{MAX_PURSE}")
    col2.metric(
        label="Endurance",
        value=f"{st.session_state.endurance}/{st.session_state.total_endurance}",
    )
    col3.metric(label="Habileté", value=st.session_state.hability)

    st.divider()
    st.subheader(f"Armes ({len(st.session_state.weapons)}/{MAX_WEAPONS})")
    if not st.session_state.weapons:
        st.error(
            "*Ne possédant aucune arme, vous subirez un malus de -4 points d'HABILETÉ au combat.*"
        )
    for index, weapon in enumerate(st.session_state.weapons):
        col1, col2 = st.columns([3, 1])
        mastered = " ⭐ *(maîtrisée)*" if is_mastered(weapon) else ""
        col1.write(f"**{weapon}**{mastered}")
        if col2.button("Jeter", key=f"drop_weapon_{index}"):
            st.session_state.weapons.pop(index)
            st.rerun()

    st.divider()
    if st.session_state.has_backpack:
        st.subheader(f"Sac à Dos ({len(st.session_state.backpack)}/{MAX_BACKPACK})")
        if not st.session_state.backpack:
            st.caption("Votre Sac à Dos est vide.")
    else:
        st.subheader("Sac à Dos")
        st.caption("Vous n'avez plus de Sac à Dos.")
    for index, item in enumerate(st.session_state.backpack):
        info = item_info(item)
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.write(f"**{item}**")
        if info.get("description"):
            col1.caption(info["description"])
        if info.get("heal"):
            if col2.button("Utiliser", key=f"use_{index}"):
                use_item(item)
                st.rerun()
        if col3.button("Jeter", key=f"drop_{index}"):
            st.session_state.backpack.pop(index)
            st.rerun()

    st.divider()
    st.subheader("Objets Spéciaux")
    if not st.session_state.special:
        st.caption("Aucun Objet Spécial.")
    for index, item in enumerate(st.session_state.special):
        info = item_info(item)
        col1, col2 = st.columns([3, 1])
        col1.write(f"**{item}**")
        if info.get("description"):
            col1.caption(info["description"])
        if col2.button("Jeter", key=f"drop_special_{index}"):
            remove_from_inventory(item)
            st.rerun()

    if st.session_state.weapon_mastery:
        st.divider()
        st.write(
            f"Vous maîtrisez : {', '.join(st.session_state.weapon_mastery)}. Combattre avec "
            "une arme que vous maîtrisez augmente votre HABILETÉ de 2 points."
        )

    st.divider()
    st.subheader("Vos Disciplines Kaï")
    for discipline in st.session_state.kai:
        st.write(f"**{discipline}**")
        st.caption(KAI.get(discipline))


def is_mastered(weapon: str) -> bool:
    return item_info(weapon).get("mastery") in st.session_state.weapon_mastery
