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

check_inventory(current_page_number=162, book=2)

fr_text = """
Il lance son cri de guerre et se rue sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Vous pouvez prendre la fuite à tout moment en vous réfugiant dans les bois ; rendez-vous "
            "pour cela au 244."
        )
    )
    outcome = combat([("CHEVALIER DE LA MONTAGNE BLANCHE", 20, 27)], flee_after=0)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
        st.page_link("tomes/tome2/page_302.py", label="302", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous vous réfugiez dans les bois. Rendez-vous au :"))
        st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
