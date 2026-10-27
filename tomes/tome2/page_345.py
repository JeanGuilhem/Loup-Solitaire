import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=345, book=2)

fr_text = """
Une bataille féroce s'est engagée sur le navire tandis que les Gloks
s'efforcent de prendre le contrôle du Sceptre Vert. Perchés en haut des
mâts, les Kraans sont en train de déchirer les voiles avec leurs serres et
leurs dents tranchantes comme des rasoirs ; pendant ce temps, les
Bêtalzans retournent vers la Pointe des Naufragés pour aller remplir
leurs filets d'autres Gloks avides de participer aux combats. Bientôt,
une silhouette menaçante apparaît sur le pont jonché de cadavres. C'est
un DRAKKARIM, un cruel guerrier à la solde des Maîtres des
Ténèbres. Il taille en pièces quiconque se trouve sur son chemin, marin
ou Glok, et s'avance vers vous en brandissant un glaive d'un noir de
jais. Parvenu devant vous, il se lance à l'attaque et il vous faut le
combattre jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DRAKKARIM", 16, 24)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome2/page_243.py", label="243", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
