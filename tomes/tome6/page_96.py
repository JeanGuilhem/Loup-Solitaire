import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=96, book=6)

fr_text = """
Une heure après le coucher du soleil, vous arrivez aux portes
d'Amory. Dans l'ombre de la tour de guet, vous attendez
patiemment que les lourds battants s'ouvrent pour vous livrer
passage. Un soldat vêtu d'une cotte de mailles noire et or
s'avance à grands pas et demande à voir votre Pass.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Pass, rendez-vous au :"))
    st.page_link("tomes/tome6/page_49.py", label="49", icon="📄", disabled=not has_item("PASS"))

    st.write_stream(stream_text("Si vous n'avez pas sur vous cet Objet Spécial, rendez-vous au :"))
    if has_item("PASS"):
        st.page_link("tomes/tome6/page_221.py", label="221", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
