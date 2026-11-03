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

check_inventory(current_page_number=226, book=4)

fr_text = """
La forêt de Ruanon est un enchevêtrement d'arbres aux troncs
gris, de toutes formes et de toutes tailles. Il vous est très difficile
de traverser cette végétation touffue et baignée de brume à dos
de cheval ; vous êtes donc bientôt contraints de mettre pied à
terre et de mener vos montures par la bride.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez continuer à progresser lentement à travers la forêt, rendez-vous au :'))
    st.page_link("tomes/tome4/page_21.py", label="21", icon="📄")

    st.write_stream(stream_text('Si vous préférez abandonner cette végétation touffue pour revenir sur la grande-route, rendez-vous au :'))
    st.page_link("tomes/tome4/page_82.py", label="82", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
