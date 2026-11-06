import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import bow_shot, called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=178, book=6)

fr_text = """
Tandis que le guerrier se dirige vers le pont au grand galop, son
manteau flotte au vent comme d'immenses ailes noires. Vous
tendez la corde de votre arc jusqu'à vos lèvres puis vous visez le
plus précisément possible. Vous n'avez droit qu'à une seule
flèche !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de la Science des Armes pour l'Arc, ajoutez 3 au chiffre obtenu."))
    total = bow_shot(key="tir")
    if total is not None:
        if total <= 7:
            st.write_stream(stream_text("Si votre total est égal ou inférieur à 7, rendez-vous au :"))
            st.page_link("tomes/tome6/page_296.py", label="296", icon="📄")
        else:
            st.write_stream(stream_text("Si votre total est supérieur ou égal à 8, rendez-vous au :"))
            st.page_link("tomes/tome6/page_303.py", label="303", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
