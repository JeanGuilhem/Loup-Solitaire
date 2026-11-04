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

check_inventory(current_page_number=262, book=5)

fr_text = """
Vous avez été repéré ; le Vordak pousse un cri horrible et
suraigu, puis pointe un doigt osseux en direction de votre
cachette. Les Drakkars se jettent dans les broussailles, se frayant
un chemin à l'aide de leurs épées noires.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez tirer votre arme et vous préparer à les affronter, rendez-vous au :"))
    st.page_link("tomes/tome5/page_212.py", label="212", icon="📄")

    st.write_stream(stream_text("Si vous préférez les fuir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_393.py", label="393", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
