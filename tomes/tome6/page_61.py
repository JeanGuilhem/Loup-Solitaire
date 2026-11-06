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

check_inventory(current_page_number=61, book=6)

fr_text = """
Grâce à votre maîtrise de cette Discipline Magnakaï, vous êtes
capable de détecter la moindre odeur d'Herbe à Potence. Au
Sommerlund, cette plante est communément appelée « Dent du
Sommeil », car on en écrase les épines pour en tirer une
substance narcotique. A l'évidence, mais pour une raison que
vous ignorez, le taxidermiste a donc l'intention de vous
endormir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez tirer votre arme et l'attaquer, rendez-vous au :"))
    st.page_link("tomes/tome6/page_277.py", label="277", icon="📄")

    st.write_stream(stream_text("Si vous préférez renverser votre gobelet et partir sans plus attendre, rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
