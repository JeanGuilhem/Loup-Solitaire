import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=34, book=2)

fr_text = """
Tandis que vous fermez la porte de votre cabine, vous entendez les cris
frénétiques de l'équipage qui se prépare à repousser les assaillants.
Soudain, un bruit sourd ébranle le navire ; quelque chose vient de
heurter le pont arrière ; retentissent alors des hurlements aigus que vous
reconnaissez aussitôt : ce sont des GLOKS qui s'égosillent ainsi ! Les
Bêtalzans ont déposé des Gloks sur le bateau et bientôt la porte de votre
cabine s'ouvre à la volée. Trois de ces hideuses créatures à la peau grise
vous font face, en brandissant leurs épées à la lame tranchante et
ruisselante de sang. Il vous est impossible de prendre la fuite et vous
allez devoir les combattre en les considérant comme un seul et même
ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GLOKS", 16, 14)])
    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur. Rendez-vous au :"))
        st.page_link("tomes/tome2/page_345.py", label="345", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
