import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=3, book=2)

fr_text = """
Vous sortez dans une petite ruelle, derrière la boutique et vous voyez,
tout au bout, un cheval attaché à un piquet par une longe.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre ce cheval et fuir le village, rendez-vous au :"))
    st.page_link("tomes/tome2/page_150.py", label="150", icon="📄")
    st.write_stream(stream_text("Si le cheval ne vous intéresse pas, quittez la ruelle et rendez-vous au :"))
    st.page_link("tomes/tome2/page_19.py", label="19", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
