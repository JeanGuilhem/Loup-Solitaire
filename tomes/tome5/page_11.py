import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=11, book=5)

fr_text = """
Pour atteindre la porte nord sans être vu, vous devez
prudemment faire le tour de la pièce en vous cachant derrière les
colonnes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Camouflage ou celle de la Chasse, déduisez 2 points du chiffre que vous avez tiré.'))
    roll = hazard_roll()
    if roll is not None:
        malus = 2 if has_kai("Le Camouflage") or has_kai("La Chasse") else 0
        total = roll - malus
        if malus:
            st.write(f"*Malus : -{malus}, soit un total de {total}.*")
        if total <= 2:
            st.write_stream(stream_text('Si le résultat obtenu est compris entre -2 et 2, rendez-vous au :'))
            st.page_link("tomes/tome5/page_167.py", label="167", icon="📄")
        else:
            st.write_stream(stream_text('Si le résultat obtenu est compris entre 3 et 9, rendez-vous au :'))
            st.page_link("tomes/tome5/page_190.py", label="190", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
