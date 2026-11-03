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

check_inventory(current_page_number=349, book=4)

fr_text = """
A en juger par l'usure du sol et des chariots de minerai, il semble
que cette galerie desserve l'un des secteurs principaux de la
mine. Un courant d'air frais souffle du tunnel orienté à l'ouest et
vous sentez que vous ne devez plus être loin de la surface.
Ruanon se trouve à l'ouest, dans la direction où mène le tunnel.
Vous prenez alors une profonde inspiration, puis, émergeant de
l'ombre, vous traversez silencieusement la galerie pour suivre la
voie ferrée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_55.py", label="55", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
