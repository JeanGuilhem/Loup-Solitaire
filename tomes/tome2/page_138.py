import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=138, book=2)

fr_text = """
Au bout d'une heure de marche, vous atteignez le sommet d'une colline.
Devant vous s'étend la forêt de Durenor. La route s'oriente vers l'est et
s'enfonce sous les arbres à proximité d'une grande tour de bois. Vous
apercevez devant la tour un soldat en faction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez poursuivre votre chemin en direction de la tour, rendez-vous au :"))
    st.page_link("tomes/tome2/page_232.py", label="232", icon="📄")
    st.write_stream(stream_text("Si vous préférez éviter le garde, faites un large détour et pénétrez dans la forêt plus loin au sud en vous rendant au :"))
    st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
