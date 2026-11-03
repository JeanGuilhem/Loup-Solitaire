import streamlit as st
from combat import combat
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

check_inventory(current_page_number=202, book=4)

fr_text = """
Vous allez devoir affronter un par un ces six Gardes lourdement
armés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [
            ("1er GARDE", 23, 24),
            ("2e GARDE", 21, 25),
            ("3e GARDE", 24, 22),
            ("4e GARDE", 18, 15),
            ("5e GARDE", 15, 16),
            ("6e GARDE", 14, 14),
        ],
        flee_after=0,
    )
    if outcome == "fled":
        st.write_stream(stream_text('Vous pouvez fuir ce combat à tout moment en sautant du pont. Rendez-vous pour cela au :'))
        st.page_link("tomes/tome4/page_342.py", label="342", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_237.py", label="237", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
