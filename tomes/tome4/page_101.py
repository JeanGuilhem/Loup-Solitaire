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

check_inventory(current_page_number=101, book=4)

fr_text = """
Vous suivez le tunnel pendant plus de deux heures avant
d'arriver dans une immense caverne. Cette grotte obscure est
séparée en deux par une rivière souterraine qui disparaît au-delà
d'une large arcade aménagée dans la paroi sud. Sur la berge
opposée vous parvenez à distinguer l'entrée d'un autre tunnel
orienté vers l'ouest. Un bateau à rames est amarré de votre côté
de la rivière et vous découvrez deux paires de rames derrière un
rocher couvert de mousse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez utiliser ce bateau pour traverser la rivière et emprunter le tunnel orienté à l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome4/page_343.py", label="343", icon="📄")

    st.write_stream(stream_text('Si vous préférez utiliser ce bateau pour suivre le cours de la rivière en direction du sud, rendez-vous au :'))
    st.page_link("tomes/tome4/page_115.py", label="115", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
