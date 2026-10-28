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

check_inventory(current_page_number=279, book=3)

fr_text = """
Les Bakanals sont réputés pour leur extraordinaire capacité de
sommeil : ils peuvent parfois dormir trois jours de suite après
avoir fait un copieux repas. Et, à en juger par la quantité d'os
fraîchement rongés qui sont répandus sur le sol, ce Bakanal ne se
réveillera probablement pas avant plusieurs heures. Vous pouvez
donc passer sans danger devant la créature et quitter les lieux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
