import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=72, book=6)

fr_text = """
Les vociférations du sergent de ville résonnent à vos oreilles
tandis que vous éperonnez votre monture vers le chariot. Vous
priez de toutes vos forces pour que votre cheval ait encore
l'énergie de franchir l'obstacle car, à présent, plus question
de reculer, il faut sauter !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï du Contrôle Animal, ajoutez 2 au chiffre que vous avez tiré."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (2 if has_magnakai("Contrôle Animal") else 0)
        st.write(f"*Total : {total}.*")
        if total <= 1:
            st.write_stream(stream_text("Si le résultat est compris entre 0 et 1, rendez-vous au :"))
            st.page_link("tomes/tome6/page_36.py", label="36", icon="📄")
        elif total <= 7:
            st.write_stream(stream_text("Si ce même résultat est compris entre 2 et 7, rendez-vous au :"))
            st.page_link("tomes/tome6/page_166.py", label="166", icon="📄")
        else:
            st.write_stream(stream_text("S'il est compris entre 8 et 11, rendez-vous au :"))
            st.page_link("tomes/tome6/page_274.py", label="274", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
