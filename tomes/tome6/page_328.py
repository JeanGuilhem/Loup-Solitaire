import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_gold,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=328, book=6)

fr_text = """
Vous vous asseyez à une table qui offre une bonne vue
d'ensemble sur la salle. Vous croisez le regard d'une serveuse et
commandez du bœuf rôti. Quelques instants plus tard, elle
revient avec une large écuelle fumante qu'elle pose devant vous.
« 2 Pièces d'Or, messire, s'il vous plaît », dit-elle en tendant la
main. Vous payez et commencez à manger. (N'oubliez pas de
rayer les Pièces d'Or de votre Feuille d'Aventure.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        if not spend_gold(2):
            lose_gold()  # le livre ne prévoit pas le cas : on donne ce qu'on a
    st.write("*2 Pièces d'Or ont été retirées de votre bourse.*")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_219.py", label="219", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
