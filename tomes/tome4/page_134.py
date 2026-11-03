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

check_inventory(current_page_number=134, book=4)

fr_text = """
Vous arrivez bientôt à l'entrée d'une galerie de mine. Deux
rangées d'empreintes de pas s'enfoncent dans l'obscurité du
tunnel. A en juger par leur forme et leur taille, elles ont été
laissées par deux de vos éclaireurs disparus. Vous criez dans la
galerie, mais personne ne vous répond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez entrer dans cette mine, rendez-vous au :'))
    st.page_link("tomes/tome4/page_91.py", label="91", icon="📄")

    st.write_stream(stream_text('Si vous préférez abandonner vos recherches, revenez le long du sentier de la colline en vous rendant au :'))
    st.page_link("tomes/tome4/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
