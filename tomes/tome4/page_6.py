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

check_inventory(current_page_number=6, book=4)

fr_text = """
Vous arrivez bientôt au croisement où le sentier aboutit à la
grand-route. Vous apercevez à nouveau le chariot brûlé,
abandonné sur le bas-côté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous n'avez pas encore examiné ce chariot, vous pouvez le faire en vous rendant au :"))
    st.page_link("tomes/tome4/page_80.py", label="80", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas y prêter attention et poursuivre votre chemin le long de la grand-route en direction du sud, rendez-vous au :"))
    st.page_link("tomes/tome4/page_175.py", label="175", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
