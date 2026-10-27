import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=19, book=2)

fr_text = """
A moins d'une vingtaine de mètres, un groupe d'hommes marche sur le
pavé mouillé ; ils sont à votre recherche ; pour tenter de leur échapper,
vous vous précipitez vers l'entrée sombre d'une petite boutique dans
laquelle vous pénétrez aussitôt. Le cœur battant à vous rompre les
côtes, vous priez le ciel qu'on ne vous ait pas repéré.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_71.py", label="71", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
