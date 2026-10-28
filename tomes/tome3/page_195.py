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

check_inventory(current_page_number=195, book=3)

fr_text = """
Au moment où vous bondissez vers l'autre bord, la glace se met à
trembler et la crevasse s'élargit soudain. Vous glissez et vous
vous cognez la tête contre le bord du gouffre béant dans lequel
vous tombez. Le lien qui attache votre ceinture à la corde de
sécurité se rompt sous le choc et vous êtes précipité dans les
ténèbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_21.py", label="21", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
