import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=63, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous êtes réveillé au milieu de la nuit par un poids qui pèse soudain sur
votre poitrine. Vous écartez lentement les pans de votre cape et vous
découvrez avec horreur qu'un Serpent des Sables s'est niché dessous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous voulez essayer d'attraper ce serpent au venin mortel juste derrière la tête et le "
            "jeter au loin, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_188.py", label="188", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez vous lever d'un bond en essayant de faire tomber le serpent sur le sol, "
            "rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_201.py", label="201", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"
        )
    )
    if has_kai("La Communication Animale"):
        st.page_link("tomes/tome2/page_264.py", label="264", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_264.py", label="264", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
