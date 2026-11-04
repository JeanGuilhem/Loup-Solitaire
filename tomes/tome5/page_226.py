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

check_inventory(current_page_number=226, book=5)

fr_text = """
Vous êtes le premier à vous ressaisir après cette brusque
rencontre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez attaquer les Gardes (en ce cas, les blessures que vous pourriez recevoir durant les 2 premiers Assauts ne vous coûteront aucun point d'ENDURANCE), rendez-vous au :"))
    st.page_link("tomes/tome5/page_334.py", label="334", icon="📄")

    st.write_stream(stream_text("Si vous ne souhaitez pas vous battre, vous pouvez fuir en remontant l'escalier avant que les Gardes ne passent à l'attaque. Rendez-vous au :"))
    st.page_link("tomes/tome5/page_209.py", label="209", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
