import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=110, book=2)

fr_text = """
Le GARDE ne vous croit pas et se rue sur vous, son épée à la main.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez prendre la fuite à tout moment."))
    outcome = combat([("GARDE DE LA TOUR", 15, 22)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous prenez la fuite : rendez-vous au :"))
        st.page_link("tomes/tome2/page_65.py", label="65", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome2/page_331.py", label="331", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
