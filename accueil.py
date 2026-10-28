import streamlit as st
from save import apply_save, page_path, read_save
from variable import BOOKS
from inventory import init_state
from utils import checkpoint_button, stream_text
from text import fr_presentation

st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
    menu_items={
        "Report a bug": "https://github.com/JeanGuilhem/Vous-tes-le-H-ros/issues",
    },
    initial_sidebar_state="collapsed",
)
st.title("Bienvenue ! ")
st.divider()

if "intro" not in st.session_state:
    st.write_stream(stream_text(text=fr_presentation))
    st.session_state.intro = True
else:
    st.write(fr_presentation)

saved_game = read_save()
if isinstance(saved_game, dict):
    book = saved_game.get("book") or 1
    page = saved_game["current_page_number"]
    where = f"paragraphe {page}" if page else "introduction"
    if st.button(f"Reprendre mon aventure (tome {book}, {where})", icon="📜"):
        init_state()
        apply_save(saved_game)
        st.session_state.game_phase = "playing"
        st.switch_page(page_path(page, book))
    st.caption("Démarrer une nouvelle aventure effacera votre sauvegarde.")

checkpoint_button()

st.page_link(
    "tomes/tome1/crafting_hero.py", label=f"Tome 1 — {BOOKS[1]['title']}", icon="⚔️"
)
st.page_link("tomes/tome2/debut.py", label=f"Tome 2 — {BOOKS[2]['title']}", icon="⛵")
st.page_link("tomes/tome3/debut.py", label=f"Tome 3 — {BOOKS[3]['title']}", icon="❄️")
st.page_link("tomes/tome1/rules.py", label="Règles", icon="🧙‍♂️")

st.caption(
    "Des statistiques de jeu anonymes (paragraphes visités, Disciplines choisies, victoires et morts) "
    "sont collectées pour améliorer l'adaptation. Aucune donnée personnelle n'est enregistrée."
)
