import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=281, book=5)

fr_text = """
Alors que vous vous apprêtez à partir, le lépreux vous fait signe
d'attendre ; d'un vieux tas de chiffons qui se trouve sous le pont,
il extrait une massue incrustée de pierreries. L'arme est en argent
massif et son manche est orné d'émeraudes et de diamants.
« Prenez cela, je vous en conjure, en signe de ma reconnaissance
éternelle. » Si vous souhaitez accepter ce présent, notez cette
Masse d'Armes incrustée sur votre Feuille d'Aventure dans la
case des Objets Spéciaux. Vous la porterez accrochée à votre
ceinture avant de quitter la grotte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("MASSE D'ARMES INCRUSTÉE", key="masse", label="Accepter la Masse d'Armes incrustée")

    st.write_stream(stream_text("Puis rendez-vous au :"))
    st.page_link("tomes/tome5/page_241.py", label="241", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
