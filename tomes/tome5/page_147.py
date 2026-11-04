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

check_inventory(current_page_number=147, book=5)

fr_text = """
Votre sens Kaï vous dit de vous méfier de l'homme qui vous a
aidé. Il a l'intention de vous trahir pour une bourse d'argent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez rester dans sa maison, rendez-vous au :"))
    st.page_link("tomes/tome5/page_61.py", label="61", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous enfuir par la fenêtre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_109.py", label="109", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
