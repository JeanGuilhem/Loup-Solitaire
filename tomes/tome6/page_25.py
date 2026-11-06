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

check_inventory(current_page_number=25, book=6)

fr_text = """
Par l'encadrement de la porte, vous apercevez une volée de marches
raides et étroites menant à une petite pièce. Deux des murs sont
couverts de livres du sol au plafond ; sur le troisième mur
s'étendent des rayonnages jonchés de manuscrits, de clochettes en
cuivre et de rouleaux de parchemin attachés par des rubans de soie
verte. Dans le dernier mur s'ouvre une petite porte par laquelle
une créature minuscule vous dévisage sans ciller. L'étrange
personnage vous prie d'entrer et vous reconnaissez, à ses yeux
rouges et son corps rabougri, qu'il s'agit d'un Kloon. « Bonjour,
étranger, dit-il d'une voix forte, contrastant avec la petitesse
de son corps. Soyez le bienvenu en notre maison. Que pouvons-nous
faire pour vous ? »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez demander au Kloon la direction de la rue des Chaudronniers, rendez-vous au :"))
    st.page_link("tomes/tome6/page_165.py", label="165", icon="📄")

    st.write_stream(stream_text("Si vous préférez lui demander de vous parler de la Pierre de la Sagesse de Varetta, rendez-vous au :"))
    st.page_link("tomes/tome6/page_262.py", label="262", icon="📄")

    st.write_stream(stream_text("Si vous n'avez aucune question à poser au Kloon, vous pouvez quitter les lieux et vous rendre au :"))
    st.page_link("tomes/tome6/page_105.py", label="105", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
