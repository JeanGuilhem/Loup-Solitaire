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

check_inventory(current_page_number=256, book=7)

fr_text = """
Vous ouvrez la porte et pénétrez dans un couloir sombre. Vous
avancez à tâtons le long du mur, guidé uniquement par une faible
lueur que vous apercevez au loin. Un brusque crissement
métallique vous fait tressaillir. En vous retournant, vous voyez,
horrifié, un mur de fer noir s'abattre devant la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_37.py", label="37", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
