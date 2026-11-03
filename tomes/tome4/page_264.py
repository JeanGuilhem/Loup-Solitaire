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

check_inventory(current_page_number=264, book=4)

fr_text = """
Votre sensibilité de Seigneur Kaï vous permet d'identifier les
traces de sabots qui longent le sentier en direction de l'est. Elles
ont été laissées par des chevaux de la cavalerie du Sommerlund.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez suivre ces traces, rendez-vous au :'))
    st.page_link("tomes/tome4/page_134.py", label="134", icon="📄")
    st.write_stream(stream_text('Si vous préférez prendre la direction opposée, rendez-vous au :'))
    st.page_link("tomes/tome4/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
