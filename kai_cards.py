"""
Choix des Disciplines Kaï en cartes cliquables (card_selector de streamlit-extras) :
création du héros (5 Disciplines), héros recréé (5) et 6e Discipline du tome 2 (1).
"""
import importlib

import streamlit as st
import streamlit_extras.card_selector as card_selector_module
from streamlit.components.v2.get_bidi_component_manager import get_bidi_component_manager

from variable import KAI_CARDS

COMPONENT_NAME = "streamlit_extras.card_selector"


def _card_selector(*args, **kwargs):
    """
    card_selector de streamlit-extras. Le composant s'enregistre auprès du runtime Streamlit à
    l'import du module : si le runtime a changé depuis (redémarrage, tests), on le réenregistre.
    """
    if get_bidi_component_manager().get(COMPONENT_NAME) is None:
        importlib.reload(card_selector_module)
    return card_selector_module.card_selector(*args, **kwargs)


def choose_disciplines(options: list, count: int, key: str) -> list:
    """
    Cartes des Disciplines `options` ; renvoie les Disciplines sélectionnées (une liste, même pour
    count = 1). Le composant ne limite pas le nombre de cartes : le compteur et le message le font,
    la page n'accepte la sélection que si elle compte exactement `count` Disciplines.
    """
    items = [
        {"icon": KAI_CARDS[name][0], "title": name, "description": KAI_CARDS[name][1]} for name in options
    ]
    if count == 1:
        index = _card_selector(items, key=key)
        selected = [] if index is None else [options[index]]
    else:
        selected = [options[index] for index in _card_selector(items, selection_mode="multi", key=key)]
        if len(selected) > count:
            st.warning(f"Vous ne pouvez maîtriser que {count} Disciplines : retirez-en {len(selected) - count}.")
        else:
            st.caption(f"Disciplines choisies : {len(selected)}/{count}")
    return selected
