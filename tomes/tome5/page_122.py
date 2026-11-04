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

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=122, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
La lourde porte de bois est renforcée par des barres de fer
maintenues par d'énormes clous de bronze. Vous tournez la
poignée, mais la porte est fermée à clé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez les Clés du Geôlier, rendez-vous au :"))
    if has_item("CLÉS DU GEÔLIER"):
        st.page_link("tomes/tome5/page_136.py", label="136", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_136.py", label="136", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'avez pas cet Objet Spécial, rendez-vous au :"))
    if has_item("CLÉS DU GEÔLIER"):
        st.page_link("tomes/tome5/page_26.py", label="26", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_26.py", label="26", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
