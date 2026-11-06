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

check_inventory(current_page_number=59, book=6)

fr_text = """
Vous sentez qu'il est temps, maintenant, de prendre une décision
: rester avec le Capitaine ou bien prendre congé de lui et
partir seul, à cheval, vers Tekaro.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous choisissez de rester avec le Capitaine, rendez-vous au :"))
    st.page_link("tomes/tome6/page_290.py", label="290", icon="📄")

    st.write_stream(stream_text("Si vous préférez le quitter pour aller de votre côté, rendez-vous au :"))
    st.page_link("tomes/tome6/page_11.py", label="11", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
