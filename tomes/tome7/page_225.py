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

check_inventory(current_page_number=225, book=7)

fr_text = """
Votre cible mobile est uniquement éclairée par la faible lumière
verte du bouclier protecteur. Vous encochez une flèche et vous
visez soigneusement la sphère qui file le long de la plage en
zigzaguant à vive allure entre les rochers.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Science des Armes avec un arc, ajoutez 3 au chiffre obtenu."))
    total = bow_shot(key="sphere")
    if total is not None:
        st.write_stream(stream_text("Si votre total est compris entre 0 et 6, rendez-vous au :"))
        st.page_link("tomes/tome7/page_196.py", label="196", icon="📄", disabled=total > 6)
        st.write_stream(stream_text("Si votre total est supérieur ou égal à 7, rendez-vous au :"))
        st.page_link("tomes/tome7/page_112.py", label="112", icon="📄", disabled=total < 7)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
