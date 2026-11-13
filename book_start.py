"""
Page de départ d'un tome à partir du 2 (tomes/tome<N>/debut.py appelle book_start(N)).
Trois façons d'y arriver :
    continue : le héros vient de finir le tome précédent (dernier paragraphe, ou sauvegarde) ;
    import   : le joueur a recréé à la main son héros du tome précédent (hero_import.py) ;
    new      : un nouveau héros vient d'être créé pour ce tome (crafting_hero.py).
Les deux premiers gardent tout et choisissent une Discipline Kaï de plus. Tous retrouvent leur
ENDURANCE maximale et reçoivent l'équipement du tome (cf. BOOK_EQUIPMENT).
À partir du tome 6 (série Magnakaï), tous choisissent les Disciplines Magnakaï qui leur manquent
(3 au tome 6, une de plus par tome) et, avec la Science des Armes, leurs armes.
"""
import streamlit as st

from game_stats import record_start
from inventory import (
    add_arrows,
    add_gold,
    add_to_inventory,
    apply_lore_circles,
    backpack_used,
    display_inventory,
    has_item,
    init_state,
    item_info,
    item_slots,
    remove_from_inventory,
)
from kai_cards import choose_disciplines
from save import apply_save, read_save
from utils import checkpoint_button, table_des_hasards
from variable import (
    BOOK_EQUIPMENT,
    BOOKS,
    KAI,
    LORE_CIRCLES,
    MAGNAKAI,
    MAGNAKAI_CARDS,
    MAGNAKAI_FROM,
    MAGNAKAI_RANKS,
    MAGNAKAI_START,
    MAGNAKAI_WEAPON_TABLE,
    MAGNAKAI_WEAPONS_START,
    MAX_BACKPACK,
    MAX_PURSE,
    MAX_WEAPONS,
    WEAPON_MASTERY_TABLE,
)

WEAPON_MASTERY = "La Maîtrise des armes"
WEAPONSKILL = "Science des Armes"


def has_finished_previous_book(state, book: int) -> bool:
    return (
        state.get("hability", 0) > 0
        and book - 1 in (state.get("completed_books") or [])
        and state.get("book", 1) == book - 1
    )


def transition_mode(book: int):
    """Comment le héros arrive à ce tome (cf. docstring), ou None s'il n'a pas encore de héros."""
    mode = st.session_state.get("transition")
    if mode is None:
        if has_finished_previous_book(st.session_state, book):
            mode = "continue"
        elif (
            st.session_state.get("game_phase") == "creation"
            and st.session_state.get("creation_book") == book
            and st.session_state.get("kai")
        ):
            mode = "new"
        else:
            return None
        st.session_state.transition = mode
    return mode


def choose_hero(book: int) -> None:
    """Pas de héros prêt pour ce tome : reprendre celui de la sauvegarde, le recréer, ou en créer un."""
    previous = book - 1
    saved = read_save()
    if saved == "pending":
        st.info("Chargement de votre sauvegarde...")
        st.stop()

    if isinstance(saved, dict) and has_finished_previous_book(saved, book):
        st.success(f"Votre héros a terminé le tome {previous} : il peut poursuivre l'aventure.")
        if st.button(f"Continuer avec mon héros du tome {previous}", icon="🐺", type="primary"):
            init_state()
            apply_save(saved)
            st.rerun()
        st.divider()

    st.write(
        f"Pour {BOOK_EQUIPMENT[book]['journey']}, il vous faut un héros. Si vous avez terminé le "
        f"tome {previous} ailleurs ou perdu votre sauvegarde, recréez votre Loup Solitaire tel qu'il "
        f"était à la fin du tome {previous}. Sinon, créez un nouveau héros."
    )
    checkpoint_button(book=book, milestone=not isinstance(saved, dict))  # le héros mort dans ce tome peut le retenter
    if isinstance(saved, dict) and not has_finished_previous_book(saved, book):
        st.warning("Votre partie en cours sera effacée.")
    col1, col2 = st.columns(2)
    col1.page_link(
        f"tomes/tome{book}/import_hero.py", label=f"Recréer mon héros du tome {previous}", icon="📝"
    )
    if col2.button("Créer un nouveau héros", icon="⚔️"):
        st.session_state.creation_request = book
        st.session_state.game_phase = None
        st.switch_page("tomes/tome1/crafting_hero.py")
    st.stop()


def show_hero() -> None:
    col1, col2, col3 = st.columns(3)
    col1.metric("Habileté", st.session_state.hability)
    col2.metric("Endurance", f"{st.session_state.endurance}/{st.session_state.total_endurance}")
    col3.metric("Couronnes", f"{st.session_state.purse}/{MAX_PURSE}")
    st.write("**Disciplines Kaï :** " + ", ".join(st.session_state.kai))
    if st.session_state.weapon_mastery:
        st.write(f"**Arme maîtrisée :** {st.session_state.weapon_mastery[0]}")
    if st.session_state.get("magnakai"):
        st.write("**Disciplines Magnakaï :** " + ", ".join(st.session_state.magnakai))
    if st.session_state.get("magnakai_weapons"):
        st.write("**Science des Armes :** " + ", ".join(st.session_state.magnakai_weapons))


def choose_new_discipline() -> bool:
    """Le héros venu du tome précédent ajoute une Discipline Kaï. Renvoie True une fois choisie."""
    if "new_kai" in st.session_state:
        st.write(f"Nouvelle Discipline Kaï : **{st.session_state.new_kai}**")
        if st.session_state.new_kai == WEAPON_MASTERY:
            st.write(
                f"*Vous avez tiré le {st.session_state.weapon_mastery_roll}* : vous maîtrisez "
                f"cette arme : **{st.session_state.weapon_mastery[0]}**"
            )
        return True

    choices = [name for name in KAI if name not in st.session_state.kai]
    if not choices:  # les Dix Disciplines sont déjà maîtrisées
        return True
    st.write(
        "Votre maîtrise des arts Kaï a progressé au cours de votre dernière mission : "
        "choisissez une nouvelle Discipline Kaï."
    )
    picked = choose_disciplines(choices, 1, key="new_kai_cards")
    choice = picked[0] if picked else None
    if choice:
        with st.expander(f"En savoir plus : {choice}"):
            st.write(KAI[choice].strip())
    if st.button("Valider ma nouvelle Discipline", type="primary", disabled=choice is None):
        st.session_state.kai.append(choice)
        st.session_state.new_kai = choice
        if choice == WEAPON_MASTERY:
            st.session_state.weapon_mastery_roll = table_des_hasards() % 10
            st.session_state.weapon_mastery = [WEAPON_MASTERY_TABLE[st.session_state.weapon_mastery_roll]]
        st.rerun()
    return False


def magnakai_needed(book: int) -> tuple:
    """(Disciplines Magnakaï, armes de la Science des Armes) qu'un héros doit avoir au début de ce tome."""
    return MAGNAKAI_START + book - MAGNAKAI_FROM, MAGNAKAI_WEAPONS_START + book - MAGNAKAI_FROM


def choose_magnakai(book: int) -> bool:
    """Le héros choisit les Disciplines Magnakaï qui lui manquent, puis ses armes. True une fois fait."""
    disciplines_needed, weapons_needed = magnakai_needed(book)
    current = st.session_state.setdefault("magnakai", [])
    if "magnakai_done" in st.session_state:
        st.write("Disciplines Magnakaï : **" + ", ".join(current) + f"** ({MAGNAKAI_RANKS[len(current)]})")
        if st.session_state.get("magnakai_weapons"):
            st.write("Science des Armes : **" + ", ".join(st.session_state.magnakai_weapons) + "**")
        for circle, (needed, hability, endurance) in LORE_CIRCLES.items():
            if set(needed) <= set(current):
                st.success(f"**{circle}** complet : +{hability} HABILETÉ, +{endurance} ENDURANCE.")
        return True

    if "magnakai_pending" not in st.session_state:
        missing = disciplines_needed - len(current)
        if missing <= 0:
            st.session_state.magnakai_pending = list(current)
            st.rerun()
        if current:
            st.write(
                "Votre maîtrise du Magnakaï a progressé au cours de votre dernière mission : choisissez "
                f"{missing} nouvelle(s) Discipline(s) Magnakaï."
            )
        else:
            st.write(
                "Après avoir étudié le Livre du Magnakaï, vous avez atteint le rang de "
                f"**{MAGNAKAI_RANKS[disciplines_needed]}** : choisissez {missing} Disciplines Magnakaï. "
                "Dans cette série, seules vos Disciplines Magnakaï comptent."
            )
        choices = [name for name in MAGNAKAI if name not in current]
        picked = choose_disciplines(choices, missing, key="magnakai_cards", cards=MAGNAKAI_CARDS)
        with st.expander("Les Cercles de Savoir"):
            st.write(
                "Si vous maîtrisez toutes les Disciplines d'un Cercle de Savoir, vous ajoutez des points "
                "à vos totaux d'HABILETÉ et d'ENDURANCE."
            )
            for circle, (needed, hability, endurance) in LORE_CIRCLES.items():
                st.write(f"**{circle}** ({', '.join(needed)}) : +{hability} HABILETÉ, +{endurance} ENDURANCE")
        valid = len(picked) == missing
        if st.button("Valider mes Disciplines Magnakaï", type="primary", disabled=not valid) and valid:
            st.session_state.magnakai_pending = current + picked
            st.rerun()
        return False

    # puis, avec la Science des Armes, les armes qui manquent
    picked = st.session_state.magnakai_pending
    st.write("Disciplines Magnakaï : **" + ", ".join(picked) + "**")
    weapons = list(st.session_state.get("magnakai_weapons", []))
    missing_weapons = weapons_needed - len(weapons) if WEAPONSKILL in picked else 0
    if missing_weapons > 0:
        weapons += st.multiselect(
            f"Science des Armes : choisissez {missing_weapons} arme(s) dont vous avez la parfaite maîtrise",
            [weapon for weapon in MAGNAKAI_WEAPON_TABLE if weapon not in weapons],
            max_selections=missing_weapons,
            key="magnakai_weapons_choice",
        )
    ready = WEAPONSKILL not in picked or len(weapons) == weapons_needed
    if missing_weapons <= 0 or st.button("Valider mes armes", type="primary", disabled=not ready):
        st.session_state.magnakai = picked
        st.session_state.magnakai_weapons = weapons if WEAPONSKILL in picked else []
        apply_lore_circles()
        st.session_state.magnakai_done = True
        st.session_state.pop("magnakai_pending")
        st.rerun()
    return False


def receive_equipment(book: int) -> bool:
    """Couronnes (gold_base + Table de Hasard) et objets au choix du tome. Renvoie True une fois reçus."""
    equipment = BOOK_EQUIPMENT[book]
    if "start_gold_roll" not in st.session_state:
        if st.button("Recevoir votre bourse", icon="💰", type="primary"):
            st.session_state.start_gold_roll = table_des_hasards() % 10
            add_gold(equipment["gold_base"] + st.session_state.start_gold_roll)
            st.rerun()
        return False
    gold = equipment["gold_base"] + st.session_state.start_gold_roll
    st.write(f"*Vous avez tiré le {st.session_state.start_gold_roll}* : vous recevez **{gold} Couronnes**.")

    if "start_items" in st.session_state:
        st.write("Vous avez choisi : **" + ", ".join(st.session_state.start_items) + "**.")
        return True

    count = equipment["items_to_choose"]
    up_to = equipment.get("up_to", False)
    options = equipment["items"]
    chosen = st.multiselect(
        f"Choisissez {'jusqu’à ' if up_to else ''}{count} objets", list(options), max_selections=count
    )
    items = [options[label] for label in chosen]
    weapons = sum(quantity for name, quantity in items if item_info(name)["type"] == "weapon")
    backpack = sum(
        quantity * item_slots(name) for name, quantity in items if item_info(name)["type"] == "backpack"
    )
    problems = []

    # « vous avez là l'occasion d'échanger l'une [de vos armes] ou les deux »
    current_weapons = list(st.session_state.weapons)
    excess = len(current_weapons) + weapons - MAX_WEAPONS
    left_behind = []  # positions dans current_weapons
    if excess == 1:
        left_behind = [
            st.radio(
                f"Vous ne pouvez porter que {MAX_WEAPONS} armes : laquelle laissez-vous à "
                f"{equipment['place']} en échange ?",
                range(len(current_weapons)),
                format_func=lambda index: current_weapons[index],
            )
        ]
    elif excess > 1:
        left_behind = list(range(len(current_weapons)))
        st.info(
            f"Vous laissez à {equipment['place']} vos armes actuelles en échange : "
            + ", ".join(current_weapons) + "."
        )
    if weapons > MAX_WEAPONS:
        problems.append(f"vous ne pouvez porter que {MAX_WEAPONS} armes")
    if backpack and not st.session_state.has_backpack:
        problems.append("vous n'avez plus de Sac à Dos")
    elif backpack_used() + backpack > MAX_BACKPACK:
        problems.append(f"votre Sac à Dos ne peut contenir que {MAX_BACKPACK} objets")
    if problems:
        st.warning(
            "Pas assez de place : " + " et ".join(problems)
            + ". Vous pouvez aussi jeter des objets depuis votre inventaire ci-dessous, "
            "ou choisir d'autres objets."
        )
    wrong_count = len(chosen) > count if up_to else len(chosen) != count
    if st.button("Prendre ces objets", disabled=wrong_count or bool(problems)):
        for weapon in [current_weapons[index] for index in left_behind]:
            remove_from_inventory(weapon)
        for name, quantity in items:
            if add_to_inventory(name, quantity=quantity, origin=equipment["origin"]) and item_info(name).get("arrows"):
                add_arrows(item_info(name)["arrows"])  # le Carquois est remis plein
        for item in equipment["special"]:
            if not has_item(item):
                add_to_inventory(item, origin=equipment["special_origins"].get(item, equipment["origin"]))
        st.session_state.start_items = chosen
        st.rerun()
    return False


def start_book(book: int) -> None:
    """Le héros part pour le paragraphe d'introduction du tome : nouvelle partie pour les statistiques."""
    mode = st.session_state.transition
    st.session_state.book = book
    st.session_state.current_page_number = 0
    st.session_state.last_page_number = 0
    st.session_state.story_flags = []  # les faits retenus ne valent que pour un tome
    st.session_state.game_phase = "playing"
    st.session_state.checkpoint_pending = True  # écrit par la page d'introduction du tome
    record_start(continued=mode != "new", items=st.session_state.start_items)
    for key in (
        "transition", "creation_book", "endurance_restored", "new_kai", "magnakai_done", "magnakai_pending", "start_gold_roll", "start_items"
    ):
        st.session_state.pop(key, None)
    st.switch_page(f"tomes/tome{book}/pages_intro.py")


def book_start(book: int) -> None:
    st.set_page_config(page_title=f"Tome {book}", page_icon="📜")
    st.title(f"📜 Tome {book} — {BOOKS[book]['title']}")

    mode = transition_mode(book)
    if mode is None:
        choose_hero(book)

    if not st.session_state.get("endurance_restored"):
        # chaque tome commence avec l'ENDURANCE au maximum
        st.session_state.endurance = st.session_state.total_endurance
        st.session_state.endurance_restored = True

    st.subheader("Votre héros")
    show_hero()
    st.divider()

    if book >= MAGNAKAI_FROM:
        st.subheader("Les Disciplines Magnakaï")
        if not choose_magnakai(book):
            st.stop()
        st.divider()
    elif mode in ("continue", "import"):
        st.subheader("Une nouvelle Discipline Kaï")
        if not choose_new_discipline():
            st.stop()
        st.divider()

    st.subheader("Votre équipement")
    if receive_equipment(book):
        st.divider()
        if st.button(BOOK_EQUIPMENT[book]["start_label"], icon="📜", type="primary"):
            start_book(book)

    with st.expander("Afficher mon inventaire"):
        display_inventory(collapsible=False)
