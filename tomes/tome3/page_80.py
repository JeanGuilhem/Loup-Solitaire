import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=80, book=3)

fr_text = """
Lorsque le Languabarb surexcité surgit du tunnel, vous attendez
le dernier moment pour faire un bond de côté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 1:
        st.write_stream(stream_text("Vous avez tiré le 0 ou le 1, rendez-vous au :"))
        st.page_link("tomes/tome3/page_123.py", label="123", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text("Vous avez tiré un chiffre entre 2 et 9, rendez-vous au :"))
        st.page_link("tomes/tome3/page_59.py", label="59", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
