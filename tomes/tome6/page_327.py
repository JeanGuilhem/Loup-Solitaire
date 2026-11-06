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

check_inventory(current_page_number=327, book=6)

fr_text = """
Au bout du couloir, deux portes se font face. La voix du
prédicateur vous parvient par le trou de serrure de la porte
droite, ce qui signifie que le temple doit se trouver de ce côté. La
porte de gauche est dépourvue de trou de serrure, mais elle ne
donne pas l'impression d'être fermée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez coller l'oreille contre la porte droite, rendez-vous au :"))
    st.page_link("tomes/tome6/page_195.py", label="195", icon="📄")

    st.write_stream(stream_text('Si vous préférez pousser la porte gauche, rendez-vous au :'))
    st.page_link("tomes/tome6/page_127.py", label="127", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
