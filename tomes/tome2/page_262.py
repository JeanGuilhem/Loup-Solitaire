import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=262, book=2)

fr_text = """
Le garde vous écarte d'une bourrade et se met à courir en direction de la
rue du Tombeau. En haut de l'escalier se trouve une petite pièce que
vous décidez de fouiller avant le retour du soldat. Vous y découvrez les
objets suivants : Épée, Masse d'Armes, Bâton, 1 Repas complet, 6
Pièces d'Or, une fiole d'un liquide orange.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si l'un ou l'autre de ces objets vous intéresse, il vous suffit de les inscrire sur votre Feuille d'Aventure pour qu'ils vous appartiennent désormais."))
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("MASSE D'ARMES", key="masse", label="Prendre la Masse d'Armes")
    pickup_button("BÂTON", key="baton", label="Prendre le Bâton")
    pickup_button("REPAS", key="repas", label="Prendre le Repas")
    pickup_gold(6, key="gold")
    pickup_button("FIOLE DE LIQUIDE ORANGE", key="fiole", label="Prendre la fiole de liquide orange")

    st.write_stream(stream_text("Lorsque vous quittez la pièce, vous vous heurtez à un autre garde ; le choc est plutôt rude et vous tombez tous deux au bas de l'escalier ; mais avant que le garde ait pu retrouver ses esprits, vous avez déjà pris la fuite en courant dans la nuit. Rendez-vous au :"))
    st.page_link("tomes/tome2/page_65.py", label="65", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
