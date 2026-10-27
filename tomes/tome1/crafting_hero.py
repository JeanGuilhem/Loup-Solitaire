import time

import streamlit as st

from game_stats import record_start
from inventory import add_gold, add_to_inventory, display_inventory, reset_state
from text import (
    fr_determine_ability_endurance,
    fr_first_items,
    fr_hazard_item,
    fr_kai_mastery,
    second_fr_kai_mastery,
)
from utils import stream_text, table_des_hasards
from variable import KAI, STARTING_ITEM_TABLE, WEAPON_MASTERY_TABLE

# Une nouvelle partie commence à chaque fois qu'on arrive sur cette page depuis ailleurs.
# Les reruns de la page (clics sur les boutons) ne doivent pas tout effacer.
# creation_request : posé par la page de départ du tome 2 juste avant d'envoyer ici, pour y créer
# un nouveau héros. Il est consommé tout de suite : la création suivante sera celle du tome 1.
if st.session_state.get("game_phase") != "creation":
    creation_book = st.session_state.pop("creation_request", 1)
    reset_state()
    st.session_state.game_phase = "creation"
    st.session_state.creation_book = creation_book


def roll() -> int:
    """Table de Hasard : chiffre de 0 à 9, comme dans le livre."""
    with st.spinner():
        time.sleep(1)
    return table_des_hasards() % 10


def write_once(key: str, text: str) -> None:
    """Affiche le texte en streaming la première fois, puis directement aux reruns suivants."""
    if key not in st.session_state:
        st.write_stream(stream_text(text))
        st.session_state[key] = True
    else:
        st.write(text)


def determine_endurance_ability() -> bool:
    """HABILETÉ = 10 + Table de Hasard, ENDURANCE = 20 + Table de Hasard. Un seul tirage chacun."""
    write_once("text_ability", fr_determine_ability_endurance)
    col1, col2 = st.columns(2)

    with col1:
        if "ability_roll" not in st.session_state:
            if st.button("Déterminer votre habileté au combat"):
                st.session_state.ability_roll = roll()
                st.session_state.hability = 10 + st.session_state.ability_roll
                st.rerun()
        else:
            st.write(f"*Vous avez tiré le {st.session_state.ability_roll}*")
            st.metric(
                label="Habileté",
                value=st.session_state.hability,
                delta=st.session_state.ability_roll,
            )

    with col2:
        if "endurance_roll" not in st.session_state:
            if st.button("Déterminer votre endurance"):
                st.session_state.endurance_roll = roll()
                st.session_state.total_endurance = 20 + st.session_state.endurance_roll
                st.session_state.endurance = st.session_state.total_endurance
                st.rerun()
        else:
            st.write(f"*Vous avez tiré le {st.session_state.endurance_roll}*")
            st.metric(
                label="Endurance",
                value=st.session_state.total_endurance,
                delta=st.session_state.endurance_roll,
            )

    return "ability_roll" in st.session_state and "endurance_roll" in st.session_state


def determine_kai_mastery() -> bool:
    """Choix des 5 Disciplines Kaï, puis tirage de l'arme si la Maîtrise des armes est choisie."""
    write_once("text_kai", second_fr_kai_mastery)

    if st.session_state.kai:
        for discipline in st.session_state.kai:
            st.write(f"- **{discipline}**")
        if st.session_state.weapon_mastery:
            st.write(
                f"*Vous avez tiré le {st.session_state.weapon_mastery_roll}*. "
                f"Vous maîtrisez cette arme : **{st.session_state.weapon_mastery[0]}**"
            )
        return True

    choices = st.multiselect(
        "Quelles Disciplines Kaï choisissez-vous ? (5 au maximum)",
        options=list(KAI.keys()),
        max_selections=5,
    )
    if st.button(
        "Valider mes Disciplines Kaï",
        disabled=len(choices) != 5,
        help="Choisissez exactement 5 Disciplines.",
    ):
        st.session_state.kai = list(choices)
        if "La Maîtrise des armes" in choices:
            st.session_state.weapon_mastery_roll = roll()
            st.session_state.weapon_mastery = [
                WEAPON_MASTERY_TABLE[st.session_state.weapon_mastery_roll]
            ]
        st.rerun()
    return False


STARTING_KIT = "Tome 1 : équipement de départ du Seigneur Kaï."
MONASTERY = "Tome 1 : trouvé dans les ruines du monastère Kaï."


def apply_starting_item(number: int) -> None:
    """Objet trouvé dans les ruines du monastère (appliqué une seule fois)."""
    found = STARTING_ITEM_TABLE[number]
    if isinstance(found, int):
        add_gold(found)
    elif found == "REPAS":
        add_to_inventory("REPAS", quantity=2, origin=MONASTERY)
    else:
        add_to_inventory(found, origin=MONASTERY)


STARTING_ITEM_TEXT = {
    1: "Vous déterrez une Épée dans les décombres de votre monastère.",
    2: "Vous déterrez un Casque et vous vous en coiffez : votre total d'ENDURANCE augmente de 2 points.",
    3: "Vous parvenez à extraire 2 Repas supplémentaires des ruines de votre monastère.",
    4: "Vous déterrez une Cotte de Mailles et vous vous en vêtez : votre total d'ENDURANCE augmente de 4 points.",
    5: "Vous déterrez une Masse d'Armes dans les décombres de votre monastère.",
    6: "Vous trouvez une Potion de Guérison encore intacte dans les décombres.",
    7: "Vous déterrez un Bâton dans les décombres de votre monastère.",
    8: "Vous déterrez une Lance dans les décombres de votre monastère.",
    9: "Vous trouvez une bourse en cuir dans laquelle se trouvent 12 Couronnes.",
    0: "Vous déterrez un Glaive dans les décombres de votre monastère.",
}


def first_inventory_check() -> bool:
    """Équipement de départ : Hache, Repas, Carte, Couronnes et un objet tiré au hasard."""
    write_once("text_first_items", fr_first_items)

    if "starting_kit" not in st.session_state:
        add_to_inventory("HACHE", origin=STARTING_KIT)
        add_to_inventory("REPAS", origin=STARTING_KIT)
        add_to_inventory("CARTE GÉOGRAPHIQUE", origin=STARTING_KIT)
        st.session_state.starting_kit = True

    col1, col2 = st.columns(2)
    col1.metric(label="Arme", value="HACHE")
    col2.metric(label="Sac à Dos", value="REPAS")

    if "gold_roll" not in st.session_state:
        if st.button("Déterminer votre nombre de Couronnes"):
            st.session_state.gold_roll = roll()
            add_gold(st.session_state.gold_roll)
            st.rerun()
        return False

    st.write(f"*Vous avez tiré le {st.session_state.gold_roll}.*")
    st.metric(label="Couronnes", value=st.session_state.gold_roll, delta=st.session_state.gold_roll)

    write_once("text_hazard_item", fr_hazard_item)
    if "item_roll" not in st.session_state:
        if st.button("Cliquez ici pour fouiller les ruines.."):
            st.session_state.item_roll = roll()
            apply_starting_item(st.session_state.item_roll)
            record_start(starting_item=STARTING_ITEM_TABLE[st.session_state.item_roll])
            st.rerun()
        return False

    st.write(f"*Vous avez tiré le {st.session_state.item_roll}.*")
    st.write(STARTING_ITEM_TEXT[st.session_state.item_roll])
    return True


tab1, tab2 = st.tabs(["Loup Solitaire", "Maîtrise Kaï"])

with tab1:
    if determine_endurance_ability():
        st.divider()
        if determine_kai_mastery():
            st.divider()
            if st.session_state.creation_book == 2:
                # l'équipement du tome 2 est remis sur sa page de départ
                st.page_link("tomes/tome2/debut.py", label="Recevoir mon équipement", icon="🎒")
            elif first_inventory_check():
                st.divider()
                with st.expander(label="Afficher mon inventaire"):
                    display_inventory()
                st.page_link(
                    "tomes/tome1/pages_intro.py", label="Commencez votre aventure", icon="📜"
                )
with tab2:
    st.write(fr_kai_mastery)
