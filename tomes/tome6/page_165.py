import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=165, book=6)

fr_text = """
« Mais certainement, noble gentilhomme ! Nous autres, de la
Guilde des Crieurs Publics, sommes toujours ravis de pouvoir
rendre service », dit le Kloon en se dandinant vers les étagères. Il
finit par en escalader une, fouiller tout en haut et en retirer une
carte, enfouie sous un amas de papier. Puis il redescend avec
agilité et dépose une mince feuille de papier à vos pieds. « Cela
fera 5 Pièces d'Or », annonce-t-il, d'une voix polie mais ferme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez acheter au Kloon son Plan de Varetta, rendez-vous au :"))
    if st.button("Payer 5 Pièces d'Or et aller au 16", disabled=st.session_state.purse < 5):
        spend_gold(5)
        st.switch_page("tomes/tome6/page_16.py")

    st.write_stream(stream_text("Si vous ne voulez pas payer ce prix, ou si vous n'en avez pas les moyens, rendez-vous au :"))
    st.page_link("tomes/tome6/page_262.py", label="262", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
