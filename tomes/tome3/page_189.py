import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=189, book=3)

fr_text = """
Vous avancez le long du couloir pendant un quart d'heure
environ, puis vous arrivez devant une immense porte de pierre
haute de 6 mètres. Vous y collez l'oreille et vous remarquez alors
qu'elle dégage une douce tiédeur. Vous sentez une vibration
parcourir la pierre et vous entendez un faible grondement. Tout
comme les autres portes d'Ikaya, celle-ci est actionnée par un
levier fixé au mur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez tirer ce levier et franchir la porte, rendez-vous au :'))
    st.page_link("tomes/tome3/page_292.py", label="292", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous en abstenir, vous pouvez retourner à la bifurcation et emprunter le passage orienté à l'est ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_97.py", label="97", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
