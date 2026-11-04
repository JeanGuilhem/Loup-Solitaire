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

check_inventory(current_page_number=334, book=5)

fr_text = """
Vous livrez bataille à deux guerriers au visage macabre. Ils
bloquent l'escalier et vous devez les combattre comme s'ils ne
faisaient qu'un.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDES DE LA TOUR", 17, 32)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous abandonnez le combat en remontant en courant l'escalier en colimaçon. Rendez-vous au :"))
        st.page_link("tomes/tome5/page_209.py", label="209", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome5/page_310.py", label="310", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
