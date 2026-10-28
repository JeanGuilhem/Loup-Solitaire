import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=202, book=3)

fr_text = """
Soudain, les rugissements des Languabarbs cessent. Ils ont senti
l'odeur d'huile de Bakanal dont votre peau est imprégnée et ils se
précipitent aussitôt sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez les combattre, rendez-vous au :"))
    st.page_link("tomes/tome3/page_263.py", label="263", icon="📄")
    st.write_stream(stream_text("Si vous préférez prendre la fuite, rendez-vous au :"))
    st.page_link("tomes/tome3/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
