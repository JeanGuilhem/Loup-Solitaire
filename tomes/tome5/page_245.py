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

check_inventory(current_page_number=245, book=5)

fr_text = """
Vous enlevez le Triangle de Pierre Bleue de votre cou et vous le
placez dans l'empreinte creusée dans le mur. Le Triangle en
épouse parfaitement la forme et la porte de pierre s'ouvre
aussitôt dans un grincement lugubre. Vous pénétrez alors dans
une pièce faiblement éclairée et vous apercevez de nombreuses
empreintes de pas dessinées dans l'épaisse couche de poussière
qui recouvre le sol de marbre. Au fond de la pièce se trouve un
trône en pierre brute, tourné vers le mur du fond. Derrière vous,
la porte se referme brusquement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_289.py", label="289", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
