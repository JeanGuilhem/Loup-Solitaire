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

check_inventory(current_page_number=142, book=3)

fr_text = """
Lorsque vous abattez votre arme sur le rocher, des centaines
d'échardes argentées jaillissent sous le coup et le bloc commence
à se fissurer, mais les Languabarbs sont déjà sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 5:
        st.write_stream(stream_text("Le bloc s'effondre et obstrue l'entrée de la grotte. Vous pouvez dès lors retourner dans l'autre tunnel en vous rendant au :"))
        st.page_link("tomes/tome3/page_284.py", label="284", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Le bloc ne tombe pas et il vous faut combattre les Languabarbs. Rendez-vous alors au :"))
        st.page_link("tomes/tome3/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
