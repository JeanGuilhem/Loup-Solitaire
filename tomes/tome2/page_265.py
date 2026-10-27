import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
check_inventory(current_page_number=265, book=2)

fr_text = """
Le soleil se couche sur le dixième jour de votre quête lorsque vous
apercevez pour la première fois la magnifique cité de Port Bax. Les
tours de la ville luisent dans la pâle clarté d'un croissant de lune comme
autant de diamants nichés au creux du rivage. Au nord se trouve le port
lui-même où sont rassemblés les vaisseaux de la puissante flotte de
guerre du royaume de Durenor. A l'est, au-delà des murs de la cité
couverts de mousse, s'étend la forêt. Enfin, au sommet d'une colline se
dresse un château de fière apparence, une haute citadelle qui donne à la
ville le plus glorieux fleuron de sa couronne. Vous pénétrez dans Port
Bax en franchissant l'une des portes aménagées dans les murs de la cité.
Il n'y a aucun garde en faction et vous passez sans difficulté. Dans la
nuit tombante, les rues qui mènent au port s'obscurcissent peu à peu.
Vous empruntez une avenue bordée d'arbres et vous remarquez bientôt
un bâtiment au toit en forme de dôme. Un large escalier de pierre donne
accès à la porte de l'édifice. Vous vous approchez et vous lisez cette
inscription gravée sur une plaque de cuivre :
HÔTEL DE VILLE
En dépit de l'heure tardive, la porte principale est toujours ouverte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans l'hôtel de ville, rendez-vous au :"))
    st.page_link("tomes/tome2/page_84.py", label="84", icon="📄")

    st.write_stream(stream_text('Si vous préférez poursuivre votre chemin en direction du port, rendez-vous au :'))
    st.page_link("tomes/tome2/page_191.py", label="191", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome2/page_252.py", label="252", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_252.py", label="252", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
