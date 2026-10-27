import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=11, book=2)

fr_text = """
Vous vous cachez dans un grand tonneau en vous dissimulant sous
votre cape de Seigneur Kaï. Mais votre tentative reste vaine car moins
d'une minute plus tard la trappe s'ouvre à la volée et les villageois
furieux sautent sur le sol de pierre en brandissant des torches et des
épées. Ils vous arrachent à votre tonneau et vous font rouler à terre à
grands coups de pied. Les cris de la foule étouffent vos supplications,
inutile d'espérer la moindre pitié. Votre quête s'achève ici, en même
temps que votre vie.
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
