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

check_inventory(current_page_number=273, book=6)

fr_text = """
« C'est la taxe que vous devez payer pour entrer à Amory,
répond-il brusquement, irrité par votre ignorance des coutumes
locales. Vous venez de Lyris, et Amory se trouve en Salonie. »
Puis il explique, tout en détachant chaque mot comme si vous étiez
sourd ou stupide: «Vous... avez... besoin... d'un... Pass...
pour... entrer... à... Amory. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Donnez-lui 3 Pièces d'Or, et rendez-vous au :"))
    if st.button("Payer 3 Pièces d'Or", disabled=st.session_state.purse < 3):
        spend_gold(3)
        st.switch_page("tomes/tome6/page_304.py")

    st.write_stream(stream_text("Si vous souhaitez continuer votre route sans payer, rendez-vous au :"))
    st.page_link("tomes/tome6/page_146.py", label="146", icon="📄")

    st.write_stream(stream_text("Si vous préférez lui donner une bonne leçon, rendez-vous au :"))
    st.page_link("tomes/tome6/page_160.py", label="160", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
