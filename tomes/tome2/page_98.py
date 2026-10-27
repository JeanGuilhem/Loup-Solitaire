import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=98, book=2)

fr_text = """
Votre Sens de l'Orientation vous indique qu'il n'y a aucun sentier dans
cette partie de la forêt de Durenor mais il vous permet de savoir quelle
direction il convient de prendre. La forêt qui s'étend devant vous est si
dense cependant qu'il vous sera impossible de la traverser à cheval.
Vous allez donc être contraint d'abandonner votre monture devant la
tour de guet, avant de poursuivre votre chemin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez vous mettre en route en direction de Port Bax, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    st.write_stream(stream_text("Si vous préférez entrer dans la tour de guet, rendez-vous au :"))
    st.page_link("tomes/tome2/page_115.py", label="115", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
