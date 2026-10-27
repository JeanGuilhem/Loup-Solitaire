import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=114, book=2)

fr_text = """
Vous avez marché pendant trois heures sur cette route déserte qui longe
la côte lorsque la nuit commence à tomber. Les terres alentour sont
plates et désolées et vous n'avez pas vu signe de vie depuis que vous
vous êtes mis en chemin. Vous décidez alors de prendre quelque repos
à l'abri des branches d'un grand arbre qui s'élève au bord de la route.
Vous posez votre tête sur votre Sac à Dos en guise d'oreiller, vous vous
couvrez de votre cape de Seigneur Kaï et vous vous laissez emporter
dans un profond sommeil.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    number = hazard_roll()
    if number is not None and number <= 3:
        st.page_link("tomes/tome2/page_206.py", label="206", icon="📄")
    elif number is not None and number <= 7:
        st.page_link("tomes/tome2/page_63.py", label="63", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome2/page_8.py", label="8", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
