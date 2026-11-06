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

check_inventory(current_page_number=163, book=6)

fr_text = """
A vingt mètres de la rive, vous entendez s'élever de grands cris : «
Arrêtez cet homme ! Arrêtez-le ! » Les Ogrons lâchent aussitôt
leurs outils et accourent au bord de l'eau. Certains d'entre eux
sont armés d'un arc qu'ils s'empressent de saisir, puis ils
commencent à tirer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Invisibilité, ajoutez 4 au nombre que vous avez tiré."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 4 if has_magnakai("Invisibilité") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Invisibilité : +{bonus}, soit un total de {total}.*")
        if total <= 3:
            st.write_stream(stream_text("Si le résultat obtenu est inférieur ou égal à 3, rendez-vous au :"))
            st.page_link("tomes/tome6/page_197.py", label="197", icon="📄")
        else:
            st.write_stream(stream_text("S'il est supérieur ou égal à 4, rendez-vous au :"))
            st.page_link("tomes/tome6/page_229.py", label="229", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
