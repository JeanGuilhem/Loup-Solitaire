import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=229, book=2)

fr_text = """
Votre Sixième Sens vous indique que ce chariot dissimule une créature
malfaisante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez aller voir de quoi il retourne, montez dans le chariot en vous rendant au :'))
    st.page_link("tomes/tome2/page_134.py", label="134", icon="📄")

    st.write_stream(stream_text('Si vous préférez prendre vos jambes à votre cou pour vous enfuir le plus vite possible, rendez-vous au :'))
    st.page_link("tomes/tome2/page_208.py", label="208", icon="📄")

    st.write_stream(stream_text("Enfin, si vous choisissez de rebrousser chemin jusqu'à la bifurcation pour prendre cette fois le tunnel de droite, vous pouvez le faire en vous rendant au :"))
    st.page_link("tomes/tome2/page_164.py", label="164", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
