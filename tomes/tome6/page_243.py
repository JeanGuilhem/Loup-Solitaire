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

check_inventory(current_page_number=243, book=6)

fr_text = """
L'haleine rance et fétide de la créature parvient à vos narines, et
vous relâchez la corde de votre Arc. Utilisez la Table de Hasard
pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï
de la Science des Armes pour l'Arc, ajoutez 3 au chiffre que vous
avez obtenu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'OCR saute les totaux 1 à 3 (« égal à 0 ») : on les envoie au 155 avec le 0
    total = bow_shot(key="tir")
    if total is not None:
        st.write_stream(stream_text("Si votre total est compris entre 0 et 3, rendez-vous au :"))
        st.page_link("tomes/tome6/page_155.py", label="155", icon="📄", disabled=total > 3)
        st.write_stream(stream_text("Si votre total est compris entre 4 et 8, rendez-vous au :"))
        st.page_link("tomes/tome6/page_292.py", label="292", icon="📄", disabled=not 4 <= total <= 8)
        st.write_stream(stream_text("Si votre total est compris entre 9 et 12, rendez-vous au :"))
        st.page_link("tomes/tome6/page_264.py", label="264", icon="📄", disabled=total < 9)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
