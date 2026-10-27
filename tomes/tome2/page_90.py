import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=90, book=2)

fr_text = """
Deux SQUALLS et trois VILLAGEOIS en colère montent les marches
quatre à quatre, bien décidés à vous faire un mauvais sort. Il vous faut
les combattre un par un.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez à tout moment prendre la fuite en sautant par une fenêtre."))
    outcome = combat(
        [
            ("1er VILLAGEOIS", 10, 16),
            ("1er SQUALL", 6, 9),
            ("2e VILLAGEOIS", 11, 14),
            ("2e SQUALL", 5, 8),
            ("3e VILLAGEOIS", 11, 17),
        ],
        flee_after=0,
    )
    if outcome == "fled":
        st.write_stream(stream_text("Vous sautez par une fenêtre ; rendez-vous au :"))
        st.page_link("tomes/tome2/page_132.py", label="132", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous parvenez à vaincre tous ces adversaires, rendez-vous au :"))
        st.page_link("tomes/tome2/page_274.py", label="274", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
