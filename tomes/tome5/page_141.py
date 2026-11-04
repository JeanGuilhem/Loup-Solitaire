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

check_inventory(current_page_number=141, book=5)

fr_text = """
Vous faites un bond de côté, évitant de justesse la flèche qui
passe en sifflant tout près de votre poitrine. « Emparez-vous de
lui, hurle Maouk, et ne le laissez pas s'enfuir, cette fois ! » Vous
êtes maintenant allongé sur le sol, à moins de 2 mètres de la
trappe.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez la soulever pour vous enfuir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_51.py", label="51", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous rendre à Maouk et à ses guerriers, rendez-vous au :"))
    st.page_link("tomes/tome5/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
