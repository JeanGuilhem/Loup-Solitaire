import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import bow_shot, called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=175, book=7)

fr_text = """
Une fumée dense s'échappe du corps de la créature que vous
venez de tuer, dissimulant de ce fait vos adversaires. Vous vous
apprêtez à tirer, mais vous êtes considérablement gêné par les
volutes âcres qui vous piquent les yeux et vous brûlent la gorge.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous ne maîtrisez pas la Discipline Magnakaï de l'Art de la Chasse avec un arc, ou si vous ne maîtrisez pas la Discipline Magnakaï de Nexus, déduisez 3 points de ce chiffre."))
    shot = bow_shot(key="tir")
    if shot is not None:
        # la fumée gêne le tir, sauf pour qui maîtrise l'Art de la Chasse ou Nexus
        penalty = 0 if has_magnakai("Art de la Chasse") or has_magnakai("Nexus") else 3
        total = shot - penalty
        if penalty:
            st.write(f"*Fumée : -3, soit un total de {total}.*")
        st.write_stream(stream_text("Si le total obtenu est inférieur ou égal à 5, rendez-vous au :"))
        st.page_link("tomes/tome7/page_19.py", label="19", icon="📄", disabled=total > 5)
        st.write_stream(stream_text("S'il est supérieur, rendez-vous au :"))
        st.page_link("tomes/tome7/page_314.py", label="314", icon="📄", disabled=total <= 5)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
