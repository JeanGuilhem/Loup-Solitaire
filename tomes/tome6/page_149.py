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

check_inventory(current_page_number=149, book=6)

fr_text = """
« Puis-je offrir un rafraîchissement avant votre départ ? vous
propose ensuite le taxidermiste. A en juger par la poussière qui
couvre vos vêtements, vous avez dû parcourir un long chemin,
n'est-ce pas ? » Sur ces mots, l'homme apporte un plateau
d'argent où sont disposés deux gobelets de cristal et une carafe
de vin. Puis il remplit les verres et il vous en tend un.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez accepter cette boisson offerte de bon cœur, rendez-vous au :"))
    st.page_link("tomes/tome6/page_228.py", label="228", icon="📄")

    st.write_stream(stream_text("Si vous préférez décliner poliment l'offre de cet homme et quitter le magasin, rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
