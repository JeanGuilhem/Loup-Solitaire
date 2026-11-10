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

check_inventory(current_page_number=317, book=7)

fr_text = """
Vous saisissez la garde du Glaive de Lumière, dégainez la lame
d'or et tranchez la vrille d'un seul coup. Mais au lieu de sang, ou
ce qui pourrait passer pour du sang dans le corps de cette
épouvantable créature, une flamme jaillit et brûle comme une
mèche. Le cerveau cesse de bouger et flotte, immobile, au-dessus
du sable, tandis que le mince tube de chair se consume
rapidement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_170.py", label="170", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
