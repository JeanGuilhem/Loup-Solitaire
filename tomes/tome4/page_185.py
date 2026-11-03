import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=185, book=4)

fr_text = """
Vous avez faim et il vous faut à présent prendre un Repas. Sinon,
vous perdrez 3 points d'ENDURANCE. Vous poursuivez ensuite
votre chemin le long du tunnel qui se prolonge sur plusieurs
kilomètres avant d'aboutir enfin à une longue galerie déserte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_40.py", label="40", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
