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

check_inventory(current_page_number=23, book=7)

fr_text = """
Les blocs de pierre d'une tour effondrée sont alignés sur la plage,
comme la colonne vertébrale d'un cadavre géant. A la lueur des
éclairs qui déchirent le ciel, vous apercevez une grande brèche
dans la forteresse de Kazan-Oud, à l'endroit où devait se dresser
la tour en question. Les vestiges d'une cage d'escalier s'élèvent de
la plage jusqu'au rempart en ruine, mais plusieurs marches
manquent, emportées selon toute vraisemblance quand la tour
s'est abattue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez tenter de monter l'escalier pour entrer dans la forteresse, rendez-vous au :"))
    st.page_link("tomes/tome7/page_150.py", label="150", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer à longer la plage, rendez-vous au :'))
    st.page_link("tomes/tome7/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
