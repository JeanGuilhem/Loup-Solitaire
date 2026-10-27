import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=248, book=2)

fr_text = """
Lorsque vous posez le Glaive d'Or sur le pont, le capitaine zombie se
rue sur vous et vous projette à terre. Il est animé d'une force
surnaturelle, impossible d'échapper à son étreinte ; il vous plonge alors
un poignard dans la gorge en éclatant d'un rire terrifiant. Votre quête
s'achève ici en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
