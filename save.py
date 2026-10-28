"""
Sauvegarde de la partie dans un cookie du navigateur.

L'état sauvegardé est un JSON (cf. SAVED_KEYS). Le cookie est lu par un composant
Streamlit asynchrone : au tout premier rendu d'une session il renvoie {} puis
relance le script une fois la vraie valeur reçue du navigateur.
"""
import datetime
import json

import extra_streamlit_components as stx
import streamlit as st

SAVE_COOKIE = "ls_save"
# Point de reprise : le héros tel qu'il était au début du tome en cours (après l'équipement).
# Il survit à la mort du héros, qui peut ainsi retenter le tome autant de fois qu'il le veut.
CHECKPOINT_COOKIE = "ls_checkpoint"
SAVE_VERSION = 1

# Clés de st.session_state qui constituent une partie
SAVED_KEYS = [
    "hability",
    "endurance",
    "total_endurance",
    "purse",
    "weapons",
    "backpack",
    "has_backpack",
    "special",
    "kai",
    "weapon_mastery",
    "current_page_number",
    "book",  # tome en cours
    "story_flags",
    "completed_books",
    "game_id",  # statistiques (cf. game_stats.py)
    "pages_visited",
    "fights",  # bilan du tome (cf. utils.show_adventure_stats)
    "enemies_defeated",
    "lowest_endurance",
    "last_recorded_page",
    "provenance",
]


def _cookie_manager() -> stx.CookieManager:
    if "cookie_manager" not in st.session_state:
        st.session_state.cookie_manager = stx.CookieManager(key="cookie_init")
    return st.session_state.cookie_manager


def book_dir(book: int = None) -> str:
    """Dossier des pages d'un tome (par défaut le tome en cours)."""
    return f"tomes/tome{book or st.session_state.get('book', 1)}"


def page_path(page_number: int, book: int = None) -> str:
    """Fichier Streamlit correspondant à un numéro de paragraphe (0 = introduction)."""
    if int(page_number) == 0:
        return f"{book_dir(book)}/pages_intro.py"
    return f"{book_dir(book)}/page_{int(page_number)}.py"


def _snapshot() -> dict:
    data = {"v": SAVE_VERSION}
    for key in SAVED_KEYS:
        data[key] = st.session_state.get(key)
    return data


def _write_cookie(name: str, data: dict, key: str) -> None:
    _cookie_manager().set(
        name,
        json.dumps(data, ensure_ascii=False),
        key=key,
        expires_at=datetime.datetime.now() + datetime.timedelta(days=365),
    )


def save_game() -> None:
    """Écrit l'état courant de la partie dans le cookie. À appeler une seule fois par rendu."""
    _write_cookie(SAVE_COOKIE, _snapshot(), key="save_game")


def save_checkpoint() -> None:
    """Point de reprise du tome en cours (cf. CHECKPOINT_COOKIE), sur la page d'introduction du tome."""
    data = _snapshot()
    st.session_state.checkpoint = data
    _write_cookie(CHECKPOINT_COOKIE, data, key="save_checkpoint")


def delete_save() -> None:
    try:
        _cookie_manager().delete(SAVE_COOKIE, key="delete_save")
    except KeyError:
        pass  # la librairie lève KeyError si le cookie n'était pas dans son cache local


def read_save():
    """
    Renvoie le dict sauvegardé, None s'il n'y a pas de sauvegarde valide,
    ou "pending" tant que le navigateur n'a pas encore transmis ses cookies.
    """
    return _read_cookie(SAVE_COOKIE, key="read_save")


def read_checkpoint():
    """Le point de reprise (dict), None s'il n'y en a pas, ou "pending" (cf. read_save)."""
    if st.session_state.get("checkpoint"):
        return st.session_state.checkpoint
    return _read_cookie(CHECKPOINT_COOKIE, key="read_checkpoint")


def _read_cookie(name: str, key: str):
    cookies = _cookie_manager().get_all(key=key)
    if not cookies:
        # Premier rendu : le composant n'a pas encore répondu. On ne conclut à l'absence
        # de sauvegarde qu'au deuxième essai.
        attempts = st.session_state.get(f"_{key}_attempts", 0) + 1
        st.session_state[f"_{key}_attempts"] = attempts
        return "pending" if attempts == 1 else None

    raw = cookies.get(name)
    if not raw:
        return None
    try:
        data = raw if isinstance(raw, dict) else json.loads(raw)
    except (TypeError, ValueError):
        return None
    if data.get("v") != SAVE_VERSION:
        return None
    return data


def apply_save(data: dict) -> None:
    """Restaure une sauvegarde dans st.session_state."""
    for key in SAVED_KEYS:
        if key in data and data[key] is not None:
            st.session_state[key] = data[key]
    # La page a déjà été « lue » : ne pas rejouer ses effets (gain d'or, perte d'ENDURANCE...)
    st.session_state.last_page_number = st.session_state.current_page_number
