import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=105, book=2)

fr_text = """
Malheureusement pour vous, la corde a été presque coupée en deux par
un coup d'épée et il faut craindre qu'elle ne casse sous votre poids.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre qui vous indiquera si la corde a tenu bon ou pas."))
    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome2/page_286.py", label="286", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome2/page_120.py", label="120", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
