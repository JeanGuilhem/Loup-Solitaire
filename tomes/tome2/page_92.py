import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=92, book=2)

fr_text = """
L'épouvantable créature pousse un dernier cri en s'écroulant à vos
pieds. Vous faites un pas en arrière pour échapper à l'odeur putride qui
se dégage de son corps en décomposition et vous voyez alors trois
autres Monstres d'Enfer s'avancer vers vous. Rester ici relèverait du
suicide et vous décidez de prendre la fuite en direction du bois après
avoir prévenu Rhygar à grands cris du danger qui menace.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_183.py", label="183", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
