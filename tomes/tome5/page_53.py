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

check_inventory(current_page_number=53, book=5)

fr_text = """
Vous reconnaissez le Signe du Poisson, symbole de l'ordre
religieux des Moines Rédempteurs. Ces derniers ont fait vœu de
silence et ils consacrent leur vie à la prière et aux pèlerinages. Ils
sont, de plus, experts dans l'art de la guérison.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans le Monastère, rendez-vous au :"))
    st.page_link("tomes/tome5/page_157.py", label="157", icon="📄")

    st.write_stream(stream_text("Si vous préférez pénétrer dans la taverne, rendez-vous au :"))
    st.page_link("tomes/tome5/page_188.py", label="188", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
