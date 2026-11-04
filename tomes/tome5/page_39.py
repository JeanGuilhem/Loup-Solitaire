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

check_inventory(current_page_number=39, book=5)

fr_text = """
L'homme est étendu à terre. Il sait que d'autres Gardes ne
tarderont pas à arriver et, à la première occasion, il tentera de se
dégager pour donner l'alarme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez continuer à l'interroger, rendez-vous au :"))
    st.page_link("tomes/tome5/page_9.py", label="9", icon="📄")
    st.write_stream(stream_text('Si vous trouvez plus prudent de vous débarrasser de lui, rendez-vous au :'))
    st.page_link("tomes/tome5/page_78.py", label="78", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
