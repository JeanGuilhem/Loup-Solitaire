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

check_inventory(current_page_number=229, book=6)

fr_text = """
Les Ogrons sont de médiocres archers et ils ne parviennent pas,
dans l'obscurité, à décocher une flèche à moins de trois mètres de
l'endroit où vous vous trouvez. Vous continuez à pagayer vers
l'autre rive et, dès que le ponton touche terre, vous sautez sur la
berge et vous avancez à travers les rochers vers la sortie des
égouts.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_249.py", label="249", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
