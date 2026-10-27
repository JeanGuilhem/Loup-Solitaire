import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=318, book=2)

fr_text = """
Vous vous trouvez dans un vaste hall entièrement désert. Face à vous,
vous apercevez deux portes sur lesquelles sont fixées des plaques de
cuivre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez franchir la porte dont la plaque indique « laissez-passer blancs », rendez-vous au :"))
    st.page_link("tomes/tome2/page_75.py", label="75", icon="📄")
    st.write_stream(stream_text("Si vous préférez pousser la porte dont la plaque indique « laissez-passer rouges », rendez-vous au :"))
    st.page_link("tomes/tome2/page_62.py", label="62", icon="📄")
    st.write_stream(stream_text("Enfin, si vous préférez ressortir et vous approcher des gardes postés au bout de la rue, rendez-vous au :"))
    st.page_link("tomes/tome2/page_246.py", label="246", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
