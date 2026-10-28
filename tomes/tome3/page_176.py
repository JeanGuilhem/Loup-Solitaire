import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=176, book=3)

fr_text = """
Vous parvenez finalement à atteindre l'autre rive et vous courez
vers l'entrée du tunnel en laissant la rivière derrière vous. Le
tunnel mène en direction du nord, et vous y marchez des heures
durant. Il vous est impossible de deviner l'heure qu'il est, car la
perpétuelle clarté qui règne dans les Grottes de Kalte ne varie
jamais, qu'il fasse jour ou nuit. A travers des fissures dans les
parois du tunnel, vous parvenez à apercevoir des salles et des
grottes, et la taille gigantesque de ce labyrinthe vous émerveille.
Vous vous endormez presque debout lorsque vous sentez soudain
une odeur de viande rôtie. Elle vient d'une grotte située à votre
droite, quelques mètres plus loin. Vous avez très faim et il va être
bientôt temps pour vous de prendre un Repas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez aller voir ce qui se passe dans cette grotte, rendez-vous au :'))
    st.page_link("tomes/tome3/page_5.py", label="5", icon="📄")
    st.write_stream(stream_text('Si vous préférez ne pas vous en occuper et poursuivre votre chemin, rendez-vous au :'))
    st.page_link("tomes/tome3/page_132.py", label="132", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
