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

check_inventory(current_page_number=273, book=4)

fr_text = """
Vous avez parcouru moins de 8 kilomètres lorsque vous
apercevez, un peu plus loin sur la grand-route, un convoi de
roulottes, peintes de couleurs voyantes et tirées par des bœufs.
Une immense bannière ornée de glands flotte sur le toit de la
roulotte de tête. On peut y lire ces mots : « Le célèbre groupe
Asajir, troubadours aux Cours Impériales de Magnamund».
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez faire signe à ces troubadours de s'arrêter pour leur poser des questions, rendez-vous au :"))
    st.page_link("tomes/tome4/page_37.py", label="37", icon="📄")
    st.write_stream(stream_text('Si vous préférez ne pas leur prêter attention et les laisser passer, rendez-vous au :'))
    st.page_link("tomes/tome4/page_126.py", label="126", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
