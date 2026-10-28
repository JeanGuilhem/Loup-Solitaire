"""
Statistiques de jeu anonymes, envoyées dans la table Supabase `game_events`.

Une partie = un identifiant aléatoire (game_id), sans aucune donnée personnelle. Événements :
    start    création du héros terminée (HABILETÉ, ENDURANCE, Disciplines, objet de départ)
    page     premier affichage d'un paragraphe (cf. end_page)
    death    mort du héros (cf. ls_death)
    victory  arrivée au dernier paragraphe du tome
Chaque événement porte le tome en cours : un héros qui passe au tome suivant y commence une
nouvelle partie (nouvel identifiant).

L'envoi se fait en arrière-plan et ne bloque jamais le jeu : sans configuration
(secrets [supabase]), avec LDVELH_STATS=off (bot de test) ou si Supabase est injoignable,
rien n'est enregistré.
"""
import os
import threading
import uuid

import requests
import streamlit as st

from variable import BOOKS

TABLE = "game_events"
TIMEOUT = 5


def _config():
    """(url de base, clé) depuis st.secrets, ou None si les statistiques sont désactivées."""
    if os.environ.get("LDVELH_STATS") == "off":
        return None
    try:
        conf = st.secrets["supabase"]
        url, key = conf["url"], conf["key"]
    except Exception:  # pas de secrets.toml, ou pas de section [supabase]
        return None
    return url.rstrip("/").removesuffix("/rest/v1"), key


def _headers(key: str) -> dict:
    return {"apikey": key, "Content-Type": "application/json"}


def _post(url: str, key: str, row: dict) -> None:
    try:
        requests.post(f"{url}/rest/v1/{TABLE}", json=row, headers=_headers(key), timeout=TIMEOUT)
    except requests.RequestException:
        pass  # une statistique perdue ne doit jamais gêner le joueur


def record(event: str, page: int = None, data: dict = None) -> None:
    """Enregistre un événement de la partie en cours, sans attendre la réponse."""
    config = _config()
    if config is None:
        return
    if "game_id" not in st.session_state:  # partie reprise d'une sauvegarde plus ancienne
        st.session_state.game_id = str(uuid.uuid4())
    row = {
        "game_id": st.session_state.game_id,
        "book": st.session_state.get("book", 1),
        "event": event,
        "page": page,
        "data": data or {},
    }
    threading.Thread(target=_post, args=(*config, row), daemon=True).start()


def record_start(**details) -> None:
    """Nouvelle partie : nouvel identifiant, puis le profil du héros et `details` (objet de départ...)."""
    st.session_state.game_id = str(uuid.uuid4())
    # bilan du tome affiché au joueur en fin de partie (cf. utils.show_adventure_stats)
    st.session_state.pages_visited = 0
    st.session_state.fights = 0
    st.session_state.enemies_defeated = 0
    st.session_state.lowest_endurance = st.session_state.get("endurance", 0)
    st.session_state.last_recorded_page = None
    record(
        "start",
        data={
            "hability": st.session_state.hability,
            "endurance": st.session_state.total_endurance,
            "kai": st.session_state.kai,
            "weapon_mastery": st.session_state.weapon_mastery,
            **details,
        },
    )


def record_page() -> None:
    """À appeler au premier affichage d'un paragraphe (cf. end_page)."""
    page = st.session_state.current_page_number
    book = st.session_state.get("book", 1)
    st.session_state.pages_visited = st.session_state.get("pages_visited", 0) + 1
    st.session_state.last_recorded_page = [book, page]
    record("page", page, {"endurance": st.session_state.endurance, "purse": st.session_state.purse})
    if page == BOOKS[book]["final_page"]:
        record(
            "victory",
            page,
            {"pages": st.session_state.pages_visited, "endurance": st.session_state.endurance},
        )


def record_death() -> None:
    """Une seule fois par partie, même si la page de mort est réaffichée."""
    if st.session_state.get("death_recorded"):
        return
    st.session_state.death_recorded = True
    record(
        "death",
        st.session_state.get("current_page_number"),
        {"pages": st.session_state.get("pages_visited", 0)},
    )


def load_events(book: int = 1) -> list:
    """Tous les événements d'un tome (pour la page de statistiques), par paquets de 1000."""
    config = _config()
    if config is None:
        return []
    url, key = config
    rows, offset, size = [], 0, 1000
    while True:
        response = requests.get(
            f"{url}/rest/v1/{TABLE}",
            params={
                "select": "game_id,event,page,data,created_at",
                "book": f"eq.{book}",
                "order": "id",
                "offset": offset,
                "limit": size,
            },
            headers=_headers(key),
            timeout=30,
        )
        response.raise_for_status()
        batch = response.json()
        rows += batch
        if len(batch) < size:
            return rows
        offset += size
