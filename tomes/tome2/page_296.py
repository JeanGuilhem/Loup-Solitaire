import streamlit as st
from combat import combat
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

check_inventory(current_page_number=296, book=2)

fr_text = """
Les clients fuient la taverne lorsque les GARDES passent à l'attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Vous pouvez prendre la fuite à tout moment en sortant par la porte de derrière ; rendez-vous alors au 88. Si vous parvenez à tuer tous les gardes, rendez-vous au 221.'))
    outcome = combat(
        [
            ("Sergent de la GARDE", 13, 22),
            ("Caporal de la GARDE", 12, 20),
            ("1er GARDE", 11, 19),
            ("2e GARDE", 11, 9),
            ("3e GARDE", 10, 18),
            ("4e GARDE", 10, 17),
        ],
        flee_after=0,
    )
    if outcome == "win":
        st.page_link("tomes/tome2/page_221.py", label="221", icon="📄")
    elif outcome == "fled":
        st.page_link("tomes/tome2/page_88.py", label="88", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
