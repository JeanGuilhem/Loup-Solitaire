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

check_inventory(current_page_number=210, book=6)

fr_text = """
A moins d'un kilomètre du village, la route s'enfonce dans une
étroite vallée. Un château à moitié en ruine se dresse sur un
piton rocheux au fond d'un précipice moussu. « Le Château de
Taunor ! s'écrie Cyrilus en se protégeant les yeux de la main.
C'est un lieu de pèlerinage pour de nombreuses gens : l'eau de sa
source thermale possède de grandes vertus curatives. » Il se
penche sur sa selle et retire un petit flacon en verre d'une
sacoche. Il vous l'offre en disant : « L'eau de Taunor peut être
utile à un guerrier tel que vous. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre le flacon pour recueillir un peu d'Eau de Taunor, rendez-vous au :"))
    st.page_link("tomes/tome6/page_63.py", label="63", icon="📄")

    st.write_stream(stream_text("Si vous préférez décliner son offre et continuer votre chemin directement vers Varetta, rendez-vous au :"))
    st.page_link("tomes/tome6/page_134.py", label="134", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
