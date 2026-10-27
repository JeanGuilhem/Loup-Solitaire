import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=127, book=2)

fr_text = """
Vous vous éveillez à l'aube, au son de la pluie qui tombe à verse sur les
pavés de la rue. Il y a maintenant six jours que vous avez quitté
Holmgard et il vous faut prendre un repas, sinon vous perdrez 3 points
d'ENDURANCE. Vous rassemblez ensuite vos affaires et vous quittez
la pièce. Tandis que vous descendez l'escalier branlant, vous apercevez
l'aubergiste qui est en train de nettoyer le carrelage à l'aide d'une
serpillière.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()
    st.write_stream(stream_text("Si vous voulez demander à l'aubergiste quel chemin prendre pour gagner Durenor, rendez-vous au :"))
    st.page_link("tomes/tome2/page_217.py", label="217", icon="📄")
    st.write_stream(stream_text("Si vous préférez quitter les lieux sans lui adresser la parole, rendez-vous au :"))
    st.page_link("tomes/tome2/page_143.py", label="143", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
