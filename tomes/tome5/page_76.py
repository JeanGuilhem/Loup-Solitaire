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

check_inventory(current_page_number=76, book=5)

fr_text = """
Vous composez le 76 sur le mécanisme et vous poussez de
l'épaule la grande porte de bronze, vous attendant à entendre le
grincement des gonds. Vous discernez en effet un léger bruit,
mais ce n'est pas celui d'une porte qui s'ouvre... Vous avez choisi
le mauvais numéro.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_98.py", label="98", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
