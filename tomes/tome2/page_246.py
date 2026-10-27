import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=246, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
L'un des gardes s'avance vers vous et demande à voir votre laissez-passer
.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous avez un laissez-passer blanc, rendez-vous au :'))
    if has_item('LAISSEZ-PASSER BLANC'):
        st.page_link("tomes/tome2/page_170.py", label="170", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_170.py", label="170", icon="📄", disabled=True)

    st.write_stream(stream_text('Si votre laissez-passer est rouge, rendez-vous au :'))
    if has_item('LAISSEZ-PASSER ROUGE'):
        st.page_link("tomes/tome2/page_202.py", label="202", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_202.py", label="202", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'avez pas de laissez-passer, l'entrée du port vous sera interdite et vous vous rendrez alors au :"))
    if has_item("LAISSEZ-PASSER BLANC") or has_item("LAISSEZ-PASSER ROUGE"):
        st.caption("Vous possédez un laissez-passer.")
        st.page_link("tomes/tome2/page_327.py", label="327", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome2/page_327.py", label="327", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
