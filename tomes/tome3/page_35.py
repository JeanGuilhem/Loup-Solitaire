import streamlit as st
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

check_inventory(current_page_number=35, book=3)

fr_text = """
Vous éprouvez le sentiment désagréable que quelqu'un vous
observe. Vous sortez de la tente et vous scrutez la nuit pour
essayer de déceler une présence, mais la neige et l'obscurité ne
laissent rien voir. A contrecœur, vous revenez à l'intérieur de la
tente et vous vous couchez, en gardant votre arme à portée de
main pour pouvoir faire face à toute attaque par surprise.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_291.py", label="291", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
