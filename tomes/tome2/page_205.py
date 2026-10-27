import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=205, book=2)

fr_text = """
L'aubergiste fronce les sourcils et vous montre du doigt une porte
latérale. « Si vous ne pouvez pas vous payer une chambre, dit-il, allez
donc dormir dans l'écurie. » En vous dirigeant vers la sortie, vous
sentez dans votre dos le regard des autres passagers de la diligence. La
porte claque sur vos talons et vous vous retrouvez seul dans la nuit
froide, le corps parcouru de frissons.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_213.py", label="213", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
