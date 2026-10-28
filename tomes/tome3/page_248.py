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

check_inventory(current_page_number=248, book=3)

fr_text = """
Vous êtes arrivé à une centaine de mètres du défilé lorsqu'un
vertige vous saisit et vous fait perdre l'équilibre. Vous essayez
désespérément de vous accrocher à la paroi rocheuse, mais vous
avez les mains engourdies par le froid et vous tombez dans la
vallée. Votre corps, parfaitement conservé dans la glace, sera
découvert par une équipe d'explorateurs dans environ deux mille
ans, à quelques années près. Il va sans dire que votre mission
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
    show_map()

end_page()
