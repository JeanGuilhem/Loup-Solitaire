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

check_inventory(current_page_number=185, book=2)

fr_text = """
Tandis que vous courez sur le pont jonché de cadavres, deux guerriers
DRAKKARIM apparaissent soudain et vous attaquent par surprise. Il
vous faut les combattre l'un après l'autre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Vous pouvez prendre la fuite à tout moment en plongeant par-dessus bord ; rendez-vous pour"
            " cela au 286."
        )
    )
    outcome = combat([("1er DRAKKARIM", 17, 25), ("2e DRAKKARIM", 16, 26)], flee_after=0)
    if outcome == "win":
        st.write_stream(
            stream_text(
                "Vous avez tué vos deux adversaires : vous pouvez sauter sur le pont d'un navire de Durenor"
                " qui passe à proximité. Rendez-vous alors au :"
            )
        )
        st.page_link("tomes/tome2/page_120.py", label="120", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous plongez par-dessus bord. Rendez-vous au :"))
        st.page_link("tomes/tome2/page_286.py", label="286", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
