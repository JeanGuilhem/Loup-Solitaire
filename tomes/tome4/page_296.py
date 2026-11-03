import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=296, book=4)

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write_stream(stream_text('Si vous possédez le Glaive de Sommer, rendez-vous au :'))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome4/page_325.py", label="325", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_325.py", label="325", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous disposez d'un flacon d'Eau Bénite, rendez-vous au :"))
    if has_item("EAU BÉNITE"):
        st.page_link("tomes/tome4/page_283.py", label="283", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_283.py", label="283", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous n'avez ni l'un ni l'autre, rendez-vous au :"))
    st.page_link("tomes/tome4/page_274.py", label="274", icon="📄", disabled=has_item("GLAIVE DE SOMMER") or has_item("EAU BÉNITE"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
