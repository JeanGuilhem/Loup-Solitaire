import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=339, book=3)

fr_text = """
Dix minutes plus tard, vos pieds et vos mains ont subi les effets
du gel. Sur cette paroi exposée, les vents glacés soufflent à plus
de 150 kilomètres à l'heure. Vous tenez bon pendant encore une
demi-heure, mais le froid a finalement raison de vous : vous
perdez connaissance et vous tombez d'une hauteur de 900
mètres. Faut-il préciser que votre mission s'achève ici en même
temps que votre vie ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
