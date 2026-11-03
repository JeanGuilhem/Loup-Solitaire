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

check_inventory(current_page_number=97, book=4)

fr_text = """
Dès que vous sortez du tunnel, vous apercevez les silhouettes de
Gardes qui s'approchent et vous vous maudissez pour avoir pris
le mauvais chemin. Vous vous êtes en effet dirigé droit vers une
patrouille. Avant que les Gardes ne vous attrapent, vous avez
cependant le temps d'essayer de vous enfuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_199.py", label="199", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
