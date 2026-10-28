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

check_inventory(current_page_number=286, book=3)

fr_text = """
La lance vous a écorché l'épaule et vous êtes projeté à terre.
Tandis que vous vous relevez tant bien que mal, l'éclaireur
Barbare s'arrête, enlève ses skis et s'avance vers vous en tenant à
la main une épée en os à l'aspect redoutable. Préparez-vous à combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_68.py", label="68", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
