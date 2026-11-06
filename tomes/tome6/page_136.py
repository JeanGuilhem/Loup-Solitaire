import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=136, book=6)

fr_text = """
Votre maîtrise de cette Discipline Magnakaï vous rend sensible à
la moindre odeur, et vous décelez aussitôt l'arôme d'Herbe à
Potence qui se dégage du breuvage que l'on vient de vous offrir.
Au Sommerlund, cette plante est communément appelée « Dent du
Sommeil », car on en écrase les épines pour en tirer une
substance narcotique. A l'évidence, mais pour des raisons que
vous ignorez, votre hôte a donc l'intention de vous endormir !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez dégainer votre arme et attaquer l'homme, rendez-vous au :"))
    st.page_link("tomes/tome6/page_66.py", label="66", icon="📄")

    st.write_stream(stream_text("Si vous préférez reposer votre gobelet sans y toucher et sortir en toute hâte du magasin du taxidermiste, rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
