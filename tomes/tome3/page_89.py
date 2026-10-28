import streamlit as st
from combat import combat
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

check_inventory(current_page_number=89, book=3)

fr_text = """
Le Barbare des Glaces se met à hurler dans votre dos, en
prononçant des paroles incompréhensibles. Vous avez été
découvert. Maudissant votre malchance, vous dégainez aussitôt
votre arme. En vous retournant, vous voyez le Barbare tirer sur
un levier fixé au mur du fond. Trois Loups Maudits apparaissent
alors dans l'encadrement d'une porte secrète qui vient de
s'ouvrir. Les trois créatures se précipitent sur vous et vous allez
devoir les combattre jusqu'à la mort, chacune à son tour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("Premier LOUP MAUDIT", 15, 24), ("Deuxième LOUP MAUDIT", 14, 23), ("Troisième LOUP MAUDIT", 14, 20)]
    )
    if outcome == "win":

        st.write_stream(stream_text('Si vous sortez vainqueur de ce combat, rendez-vous au :'))
        st.page_link("tomes/tome3/page_161.py", label="161", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
