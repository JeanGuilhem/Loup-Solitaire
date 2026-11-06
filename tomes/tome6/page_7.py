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

check_inventory(current_page_number=7, book=6)

fr_text = """
Vous sentez régner une extrême tension et votre instinct de Maître
Kaï Principal vous prévient d'un danger imminent. La sérénité de
ce petit hameau est trompeuse et cache en réalité une menace
mortelle. Vous dégainez immédiatement votre arme et vous vous
préparez à affronter le péril.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_258.py", label="258", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
