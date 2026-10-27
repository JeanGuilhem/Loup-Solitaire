import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=82, book=2)

fr_text = """
Lorsque vous êtes assuré que la populace s'est bel et bien éloignée,
vous sautez de la meule et vous courez le long de la rue en vous
dissimulant dans l'ombre et en prenant bien garde à ne pas faire de
bruit. Bientôt, vous apercevez sur votre gauche une boutique qui porte
cette enseigne :
La vitrine de la boutique est éclairée et la porte ouverte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez entrer dans les lieux, rendez-vous au :"))
    st.page_link("tomes/tome2/page_55.py", label="55", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer à courir le long de la rue, rendez-vous au :"))
    st.page_link("tomes/tome2/page_347.py", label="347", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
