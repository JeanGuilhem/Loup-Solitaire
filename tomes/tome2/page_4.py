import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=4, book=2)

fr_text = """
La taverne est remplie de brigands et d'ivrognes. Il y a là tous les bons à
rien qui ont réussi à se faire engager dans les équipages des navires
marchands amarrés dans le port. La plupart d'entre eux sont en train de
boire et de chanter tandis que d'autres se mesurent au bras de fer. Tous
sont si occupés que votre entrée passe inaperçue. Dans un coin, vous
apercevez les pêcheurs qui vous ont volé. Ils sont assis autour d'une
table encombrée de chopes de bière vides. Si vous voulez atteindre le
Royaume de Durenor à temps, il vous faut à tout prix récupérer le
Sceau d'Hammardal, ainsi que vos Pièces d'Or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez affronter les pêcheurs, rendez-vous au :"))
    st.page_link("tomes/tome2/page_104.py", label="104", icon="📄")
    st.write_stream(stream_text("Si vous jugez préférable de parler à l'aubergiste, rendez-vous au :"))
    st.page_link("tomes/tome2/page_342.py", label="342", icon="📄")
    st.write_stream(stream_text("Enfin, si vous voulez plutôt essayer de gagner quelques Pièces d'Or en engageant une partie de bras de fer, rendez-vous au :"))
    st.page_link("tomes/tome2/page_276.py", label="276", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
