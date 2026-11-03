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

check_inventory(current_page_number=216, book=4)

fr_text = """
On ne peut plus faire grand-chose pour aider le patrouilleur
blessé. Des tentacules entourent à présent le bateau de tous côtés
et vous risquez à tout moment d'être précipité dans l'eau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez venir en aide à l'autre patrouilleur qu'un tentacule enroulé autour de son pied essaie d'attirer dans la rivière, rendez-vous au :"))
    st.page_link("tomes/tome4/page_304.py", label="304", icon="📄")

    st.write_stream(stream_text("Si vous préférez empoigner les rames et tenter d'amener le bateau jusqu'à la rive opposée, rendez-vous au :"))
    st.page_link("tomes/tome4/page_189.py", label="189", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
