import streamlit as st
from inventory import (
    check_inventory,
    completed_lore_circles,
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

check_inventory(current_page_number=328, book=7)

fr_text = """
Les créatures s'avancent le long de l'étroit passage et sont une
cible facile pour votre arc.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # « Art de la Chasse avec un arc » : coquille pour la Science des Armes à l'Arc, que bow_shot ajoute seul
    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de la Science des Armes avec un arc, ajoutez 3 au chiffre obtenu. Si vous avez complété le Cercle de Savoir du Feu, ajoutez 1."))
    shot = bow_shot(key="tir")
    if shot is not None:
        total = shot + (1 if "Cercle de Feu" in completed_lore_circles() else 0)
        if total != shot:
            st.write(f"*Cercle du Feu : {shot} + 1 = **{total}**.*")
        st.write_stream(stream_text("Si votre total est compris entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome7/page_232.py", label="232", icon="📄", disabled=total > 4)
        st.write_stream(stream_text("S'il est égal ou supérieur à 5, rendez-vous au :"))
        st.page_link("tomes/tome7/page_67.py", label="67", icon="📄", disabled=total <= 4)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
