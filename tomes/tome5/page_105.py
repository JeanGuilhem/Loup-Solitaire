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

check_inventory(current_page_number=105, book=5)

fr_text = """
Parmi les nombreuses sculptures situées dans les niches du mur
orienté au sud, votre attention est attirée par un buste en
marbre. En l'examinant de plus près, vous apercevez une
charnière à la base du cou. Vous faites basculer la tête en arrière
et vous notez la présence d'un petit levier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez tirer le levier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_171.py", label="171", icon="📄")

    st.write_stream(stream_text("Si vous préférez remettre la tête en place et continuer à longer la galerie, rendez-vous au :"))
    st.page_link("tomes/tome5/page_158.py", label="158", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
