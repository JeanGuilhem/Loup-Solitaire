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

check_inventory(current_page_number=157, book=5)

fr_text = """
Une forte odeur d'encens brûlé remplit la maison. Vous entrez
dans un couloir bordé de chaises et vous avancez lentement le
long de l'allée centrale vers une fontaine flanquée de deux
colonnes rouge orangé. Un homme vêtu de noir des pieds à la
tête apparaît derrière la colonne de gauche et s'avance vers vous.
Soudain, vous entendez les hommes de Maouk arriver sur la
place et jeter des regards inquiets vers la porte ouverte. L'homme
voit que vous êtes nerveux et indique silencieusement la porte
d'une cave.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez vous cacher dans la cave, rendez-vous au :'))
    st.page_link("tomes/tome5/page_16.py", label="16", icon="📄")

    st.write_stream(stream_text('Si vous préférez quitter les lieux, retournez à la Grand-Place en vous rendant au :'))
    st.page_link("tomes/tome5/page_99.py", label="99", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
