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

check_inventory(current_page_number=226, book=6)

fr_text = """
Vous essayez de pousser les grandes portes, mais elles ne
s'ouvrent pas : elles sont fermées à clé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez frapper aux portes du temple, rendez-vous au :"))
    st.page_link("tomes/tome6/page_242.py", label="242", icon="📄")

    st.write_stream(stream_text("Si vous préférez maintenant essayer d'entrer dans l'observatoire, rendez-vous au :"))
    st.page_link("tomes/tome6/page_127.py", label="127", icon="📄")

    st.write_stream(stream_text("Enfin, si vous voulez suivre le couloir qui longe le temple, rendez-vous au :"))
    st.page_link("tomes/tome6/page_327.py", label="327", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
