"""
Moteur de combat du Loup Solitaire (cf. « Règles de combat » et « Possibilités de fuite »).

Utilisation dans une page :

    outcome = combat([("KRAAN", 16, 24)], hability_modifier=-1)
    if outcome == "win":
        st.page_link("tomes/tome1/page_XXX.py", label="XXX", icon="📄")

combat() affiche l'écran de combat et renvoie None tant que le combat n'est pas terminé, puis
l'issue : "win", "fled", "rounds_over" (max_rounds atteint) ou "wounded" (stop_when_wounded).
L'ENDURANCE du Loup Solitaire est mise à jour à chaque assaut ; s'il meurt, la page s'arrête.
"""
import streamlit as st

from inventory import (
    change_endurance,
    has_item,
    has_kai,
    is_mastered,
    item_info,
    remove_from_inventory,
)
from utils import table_des_hasards

SOMMERSWERD = "GLAIVE DE SOMMER"

KILL = None  # « T » dans la table : tué sur le coup

# Table des coups portés (fin du livre). Colonnes : quotient d'attaque
# ≤-11, -10/-9, -8/-7, -6/-5, -4/-3, -2/-1, 0, +1/+2, +3/+4, +5/+6, +7/+8, +9/+10, ≥+11.
# Lignes : chiffre de la Table de Hasard (0 à 9). Cellules : (pertes Ennemi, pertes Loup Solitaire).
# fmt: off
_K = KILL
COMBAT_RESULTS_TABLE = {
    1: [(0, _K), (0, _K), (0, 8), (0, 6), (1, 6), (2, 5), (3, 5), (4, 5), (5, 4), (6, 4), (7, 4), (8, 3), (9, 3)],
    2: [(0, _K), (0, 8), (0, 7), (1, 6), (2, 5), (3, 5), (4, 4), (5, 4), (6, 3), (7, 3), (8, 3), (9, 3), (10, 2)],
    3: [(0, 8), (0, 7), (1, 6), (2, 5), (3, 5), (4, 4), (5, 4), (6, 3), (7, 3), (8, 3), (9, 2), (10, 2), (11, 2)],
    4: [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 4), (6, 3), (7, 3), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2)],
    5: [(1, 7), (2, 6), (3, 5), (4, 4), (5, 4), (6, 3), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (14, 1)],
    6: [(2, 6), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 2), (9, 2), (10, 2), (11, 1), (12, 1), (14, 1), (16, 1)],
    7: [(3, 5), (4, 5), (5, 4), (6, 3), (7, 2), (8, 2), (9, 1), (10, 1), (11, 1), (12, 0), (14, 0), (16, 0), (18, 0)],
    8: [(4, 4), (5, 4), (6, 3), (7, 2), (8, 1), (9, 1), (10, 0), (11, 0), (12, 0), (14, 0), (16, 0), (18, 0), (_K, 0)],
    9: [(5, 3), (6, 3), (7, 2), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (14, 0), (16, 0), (18, 0), (_K, 0), (_K, 0)],
    0: [(6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (14, 0), (16, 0), (18, 0), (_K, 0), (_K, 0), (_K, 0)],
}
# fmt: on


def _column(quotient: int) -> int:
    if quotient <= -11:
        return 0
    if quotient >= 11:
        return 12
    if quotient == 0:
        return 6
    if quotient < 0:
        return 5 - (-quotient - 1) // 2
    return 7 + (quotient - 1) // 2


def table_coups(quotient_attaque: int, dice_number: int) -> tuple:
    """
    Résultat d'un assaut : (pertes Ennemi, pertes Loup Solitaire), KILL (None) = tué sur le coup.
    dice_number : chiffre de la Table de Hasard, 0 à 9 (10 est accepté et vaut 0).
    """
    return COMBAT_RESULTS_TABLE[dice_number % 10][_column(quotient_attaque)]


def combat_hability(
    hability_modifier: int = 0,
    psychic_immune: bool = False,
    psychic_attack: bool = False,
) -> tuple:
    """HABILETÉ de combat du Loup Solitaire et détail des bonus/malus appliqués."""
    hability = st.session_state.hability
    details = [f"HABILETÉ de base : {hability}"]

    def apply(points: int, reason: str):
        nonlocal hability
        hability += points
        details.append(f"{reason} : {points:+d}")

    if hability_modifier:
        apply(hability_modifier, "Situation")
    weapons = combat_weapons()
    if not weapons:
        apply(-4, "Combat à mains nues")
    elif has_kai("La Maîtrise des armes") and any(is_mastered(weapon) for weapon in weapons):
        apply(2, "Maîtrise des armes")
    for item in st.session_state.special:
        if item_info(item).get("combat_bonus"):
            apply(item_info(item)["combat_bonus"], item.capitalize())
    if has_kai("Puissance psychique"):
        if psychic_immune:
            details.append("Puissance psychique : sans effet sur cet ennemi")
        else:
            apply(2, "Puissance psychique")
    if psychic_attack:
        if has_kai("Bouclier psychique"):
            details.append("Bouclier psychique : vous protège de l'attaque mentale")
        elif has_item(SOMMERSWERD):
            details.append("Glaive de Sommer : vous protège de la magie ennemie")
        else:
            apply(-2, "Attaque psychique ennemie")
    return hability, details


def combat_weapons() -> list:
    """Armes utilisables en combat : la case Armes, plus les Objets Spéciaux qui sont des armes."""
    return st.session_state.weapons + [
        item for item in st.session_state.special if item_info(item).get("weapon")
    ]


def protected_from_magic() -> bool:
    """Bouclier psychique, ou Glaive de Sommer qui « rend nulle toute pratique magique »."""
    return has_kai("Bouclier psychique") or has_item(SOMMERSWERD)


def combat(
    enemies: list,
    key: str = "combat",
    hability_modifier: int = 0,
    first_round_modifier: int = 0,
    psychic_immune: bool = False,
    psychic_attack: bool = False,
    psychic_attack_from_round: int = 1,
    flee_after: int = None,
    max_rounds: int = None,
    stop_when_wounded: bool = False,
    psychic_damage: int = 0,
    undead: bool = False,
    ls_immune_rounds: int = 0,
):
    """
    enemies               : [(NOM, HABILETÉ, ENDURANCE), ...] combattus l'un après l'autre.
    key                   : identifiant unique si la page contient plusieurs combats.
    hability_modifier     : bonus/malus d'HABILETÉ imposé par le texte pour tout le combat.
    first_round_modifier  : bonus/malus supplémentaire pour le premier assaut seulement.
    psychic_immune        : l'ennemi est insensible à la Puissance psychique.
    psychic_attack        : l'ennemi attaque par la pensée (-2 HABILETÉ sans Bouclier psychique).
    psychic_attack_from_round : assaut à partir duquel l'attaque psychique s'applique.
    flee_after            : None = fuite impossible, 0 = à tout moment, N = après N assauts.
    max_rounds            : le combat s'arrête après N assauts ("rounds_over" si l'ennemi vit encore).
    stop_when_wounded     : le combat s'arrête dès que le Loup Solitaire perd de l'ENDURANCE.
    psychic_damage        : ENDURANCE perdue en plus à chaque assaut par la Force Mentale ennemie
                            (« si vous ne maîtrisez pas le Bouclier Psychique, vous perdrez 2 points
                            d'ENDURANCE supplémentaires à chaque assaut »).
    undead                : mort vivant (Monstre d'Enfer, Zombie...) : avec le Glaive de Sommer, ses
                            pertes d'ENDURANCE sont multipliées par 2.
    ls_immune_rounds      : le Loup Solitaire ne perd aucun point d'ENDURANCE pendant les N premiers
                            assauts (ennemi surpris, incapable de se défendre).
    """
    st.session_state.page_has_fight = True  # pas de Guérison sur ce paragraphe
    state_key = f"combat_{key}"
    if state_key not in st.session_state:
        st.session_state[state_key] = {
            "status": "setup",
            "enemy": 0,
            "enemy_endurance": enemies[0][2],
            "round": 0,
            "item_bonus": 0,
            "log": [],
            "outcome": None,
        }
    fight = st.session_state[state_key]
    hability, details = combat_hability(hability_modifier, psychic_immune, False)
    psychic_malus = psychic_attack and not protected_from_magic()
    rules = {
        "psychic_damage": 0 if protected_from_magic() else psychic_damage,
        "enemy_multiplier": 2 if undead and has_item(SOMMERSWERD) else 1,
        "ls_immune_rounds": ls_immune_rounds,
    }

    def round_hability(round_number: int) -> int:
        value = hability + fight["item_bonus"]
        if round_number == 1:
            value += first_round_modifier
        if psychic_malus and round_number >= psychic_attack_from_round:
            value -= 2
        return value

    _display_enemies(enemies, fight)

    if fight["status"] == "setup":
        if psychic_attack:
            details.append(
                "Bouclier psychique : vous protège de l'attaque mentale"
                if not psychic_malus
                else "Attaque psychique ennemie : -2"
                + (f" (à partir de l'assaut {psychic_attack_from_round})" if psychic_attack_from_round > 1 else "")
            )
        if first_round_modifier:
            details.append(f"Premier assaut : {first_round_modifier:+d}")
        if psychic_damage:
            details.append(
                f"Force Mentale ennemie : -{psychic_damage} ENDURANCE par assaut"
                if rules["psychic_damage"]
                else "Force Mentale ennemie : sans effet sur vous"
            )
        if rules["enemy_multiplier"] > 1:
            details.append("Glaive de Sommer : pertes du mort vivant ×2")
        if ls_immune_rounds:
            details.append(f"Effet de surprise : aucune perte d'ENDURANCE pendant {ls_immune_rounds} assaut(s)")
        st.caption(" · ".join(details))

        fight_items = [
            item
            for item in st.session_state.backpack + st.session_state.special
            if item_info(item).get("combat_hability")
        ]
        chosen = []
        for index, item in enumerate(fight_items):
            bonus = item_info(item)["combat_hability"]
            if st.checkbox(f"Utiliser {item} ({bonus:+d} HABILETÉ pour ce combat)", key=f"{state_key}_item_{index}"):
                chosen.append(item)

        col1, col2 = st.columns(2)
        if col1.button("⚔️ Commencer le combat", key=f"{state_key}_start", type="primary"):
            for item in chosen:
                if remove_from_inventory(item):
                    fight["item_bonus"] += item_info(item)["combat_hability"]
            fight["status"] = "fighting"
            st.rerun()
        if flee_after == 0 and col2.button("🏃 Prendre la fuite", key=f"{state_key}_flee_now"):
            fight["status"], fight["outcome"] = "over", "fled"
            st.rerun()
        return None

    next_round = fight["round"] + 1 if fight["status"] == "fighting" else fight["round"]
    _display_log(fight, round_hability(next_round))
    feedback = fight.pop("feedback", None)
    if feedback:
        st.toast(feedback["text"], icon=feedback["icon"])

    if fight["status"] == "fighting":
        can_flee = flee_after is not None and fight["round"] >= flee_after
        col1, col2, col3 = st.columns(3)
        if col1.button("⚔️ Assaut suivant", key=f"{state_key}_round", type="primary"):
            entries = [_play_round(fight, enemies, round_hability, max_rounds, stop_when_wounded, rules=rules)]
            _set_feedback(fight, entries)
            st.rerun()
        if col2.button("⏩ Combattre jusqu'au bout", key=f"{state_key}_auto"):
            entries = []
            while fight["status"] == "fighting":
                entries.append(_play_round(fight, enemies, round_hability, max_rounds, stop_when_wounded, rules=rules))
            _set_feedback(fight, entries)
            st.rerun()
        if flee_after is not None:
            label = "🏃 Prendre la fuite" if can_flee else f"🏃 Fuite possible après {flee_after} assaut(s)"
            if col3.button(label, key=f"{state_key}_flee", disabled=not can_flee):
                entries = [
                    _play_round(fight, enemies, round_hability, max_rounds, stop_when_wounded, fleeing=True, rules=rules)
                ]
                _set_feedback(fight, entries)
                st.rerun()
        return None

    if st.session_state.endurance <= 0:
        change_endurance(0)  # mort : affiche le message et arrête la page
    messages = {
        "win": ("success", "Vous êtes vainqueur !"),
        "fled": ("warning", "Vous prenez la fuite."),
        "rounds_over": ("info", "Votre adversaire est toujours en vie."),
        "wounded": ("warning", "Vous avez été blessé au cours du combat."),
    }
    level, message = messages[fight["outcome"]]
    getattr(st, level)(message)
    return fight["outcome"]


def _set_feedback(fight, entries) -> None:
    """Prépare le pop-up affiché après un ou plusieurs assauts (montré au rendu suivant)."""
    ls_loss = sum(entry["ls_loss"] for entry in entries)
    fight["last_loss"] = ls_loss
    fight["last_enemy_losses"] = {}
    for entry in entries:
        index = entry["enemy_index"]
        fight["last_enemy_losses"][index] = fight["last_enemy_losses"].get(index, 0) + entry["enemy_loss"]
    if len(entries) == 1:
        entry = entries[0]
        enemy_part = "vous fuyez" if entry["fleeing"] else f"{entry['enemy']} perd {entry['enemy_loss']}"
        text = f"Assaut {entry['round']} : "
        text += f"**-{ls_loss} ENDURANCE**" if ls_loss else "**aucune blessure**"
        text += f" · {enemy_part}"
    else:
        text = f"{len(entries)} assauts : " + (
            f"**-{ls_loss} ENDURANCE** au total" if ls_loss else "**aucune blessure**"
        )
    fight["feedback"] = {"text": text, "icon": "💥" if ls_loss else "🛡️"}


def _play_round(fight, enemies, round_hability, max_rounds, stop_when_wounded, fleeing=False, rules=None):
    """Joue un assaut, met à jour l'état du combat et l'ENDURANCE du Loup Solitaire, renvoie l'entrée du journal."""
    fight["round"] += 1
    enemy_index = fight["enemy"]
    name, enemy_hability, _ = enemies[enemy_index]
    hability = round_hability(fight["round"])
    quotient = hability - enemy_hability
    dice = table_des_hasards() % 10
    enemy_loss, ls_loss = table_coups(quotient, dice)

    rules = rules or {}
    if fight["round"] <= rules.get("ls_immune_rounds", 0):
        ls_loss = 0
    elif ls_loss is KILL:
        ls_loss = st.session_state.endurance
    else:
        ls_loss += rules.get("psychic_damage", 0)
    if fleeing:
        enemy_loss = 0  # en fuyant, seul le Loup Solitaire subit des pertes
    elif enemy_loss is KILL:
        enemy_loss = fight["enemy_endurance"]
    else:
        enemy_loss *= rules.get("enemy_multiplier", 1)
    enemy_loss = min(enemy_loss, fight["enemy_endurance"])

    st.session_state.endurance = max(0, st.session_state.endurance - ls_loss)
    fight["enemy_endurance"] -= enemy_loss
    entry = {"round": fight["round"], "enemy": name, "enemy_index": enemy_index, "quotient": quotient, "dice": dice,
             "ls_loss": ls_loss, "enemy_loss": enemy_loss, "fleeing": fleeing}
    fight["log"].append(entry)
    _update_status(fight, enemies, ls_loss, fleeing, max_rounds, stop_when_wounded)
    return entry


def _update_status(fight, enemies, ls_loss, fleeing, max_rounds, stop_when_wounded) -> None:
    """Détermine si le combat continue après l'assaut qui vient d'être joué."""
    if st.session_state.endurance <= 0:
        fight["status"], fight["outcome"] = "over", "dead"
        return
    if stop_when_wounded and ls_loss > 0:
        fight["status"], fight["outcome"] = "over", "wounded"
        return
    if fleeing:
        fight["status"], fight["outcome"] = "over", "fled"
        return
    if fight["enemy_endurance"] <= 0:
        fight["enemy"] += 1
        if fight["enemy"] >= len(enemies):
            fight["status"], fight["outcome"] = "over", "win"
            return
        fight["enemy_endurance"] = enemies[fight["enemy"]][2]
    if max_rounds is not None and fight["round"] >= max_rounds:
        fight["status"], fight["outcome"] = "over", "rounds_over"


def _display_enemies(enemies, fight):
    last_losses = fight.get("last_enemy_losses", {})
    for index, (name, hability, endurance) in enumerate(enemies):
        if index < fight["enemy"]:
            current = 0
        elif index == fight["enemy"]:
            current = fight["enemy_endurance"]
        else:
            current = endurance
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.subheader(("☠️ " if current <= 0 else "") + name)
        col2.metric(label="Habileté", value=hability)
        loss = last_losses.get(index)
        col3.metric(label="Endurance", value=f"{current}/{endurance}", delta=-loss if loss else None)


def _display_log(fight, hability):
    col1, col2 = st.columns(2)
    last_loss = fight.get("last_loss")
    col1.metric(
        label="Votre Endurance",
        value=f"{st.session_state.endurance}/{st.session_state.total_endurance}",
        delta=-last_loss if last_loss else None,
    )
    col2.metric(label="Votre Habileté de combat", value=hability)
    if not fight["log"]:
        return
    with st.expander("Déroulé du combat", expanded=True):
        for entry in fight["log"]:
            enemy_part = (
                "vous fuyez"
                if entry["fleeing"]
                else f"{entry['enemy']} perd **{entry['enemy_loss']}**"
            )
            st.markdown(
                f"Assaut {entry['round']} — quotient {entry['quotient']:+d}, chiffre **{entry['dice']}** : "
                f"vous perdez **{entry['ls_loss']}**, {enemy_part}"
            )
