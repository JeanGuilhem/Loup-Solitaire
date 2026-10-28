import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=138, book=3)

fr_text = """
Vous avez pris les Languabarbs par surprise et vous parvenez à
tuer l'un d'eux avant que les autres n'aient le temps de réagir. Les
deux créatures vous attaquent l'une après l'autre en essayant de
vous piquer avec les poils rêches qui leur couvrent la langue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("Premier LANGUABARB", 11, 35), ("Deuxième LANGUABARB", 10, 32)],
        stop_when_wounded=True,
        flee_after=0,
    )
    if outcome == "wounded":
        st.write_stream(stream_text("Vous avez perdu des points d'ENDURANCE au cours de ce combat : rendez-vous immédiatement au :"))
        st.page_link("tomes/tome3/page_66.py", label="66", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Vous l'emportez sans perdre un seul point d'ENDURANCE : rendez-vous au :"))
        st.page_link("tomes/tome3/page_25.py", label="25", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous prenez la fuite en vous rendant au :"))
        st.page_link("tomes/tome3/page_277.py", label="277", icon="📄")
    else:
        st.caption("Vous avez le droit de prendre la fuite (277).")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
