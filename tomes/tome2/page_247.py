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

check_inventory(current_page_number=247, book=2)

fr_text = """
Vous êtes comme hypnotisé par ce mât qui tombe sur vous et vous
n'avez même plus la force de faire un geste. Le capitaine et ses hommes
d'équipage, impuissants à vous porter secours, voient avec horreur
l'énorme masse de bois s'écraser sur vous. La mort est instantanée.
Votre mission s'achève ici en même temps que votre vie.
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
