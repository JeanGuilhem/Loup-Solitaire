import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import ls_death, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=37, book=3)

fr_text = """
Dans l'obscurité, vous n'avez pas vu une étroite et profonde
crevasse qui se dissimulait dans le sol de glace. Vous tombez
dedans, vous faites une chute de plus de 15 mètres, et vous
atterrissez sur des rochers pointus en vous cassant les deux
jambes. Vous êtes immobilisé et il n'y a personne pour venir à
votre secours. Votre mission s'achève donc ici en même temps
que votre vie.
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
