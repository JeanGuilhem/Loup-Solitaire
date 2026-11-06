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

check_inventory(current_page_number=216, book=6)

fr_text = """
Vous concentrez tous vos pouvoirs de Science Médicale, puis
vous transmettez la chaleur bienfaisante créée par votre Art
Magnakaï au corps du magicien. Ses frêles épaules tremblent
tandis qu'il s'efforce de murmurer une dernière fois : « La rue
des Chaudronniers... Varetta cherchez... Gwinian le Sage, il vous
aidera... dans vos recherches. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_46.py", label="46", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
