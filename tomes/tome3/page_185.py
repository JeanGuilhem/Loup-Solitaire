import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=185, book=3)

fr_text = """
Vous concentrez votre énergie sur la serrure, mais il vous est
difficile de vous en représenter le mécanisme interne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Sixième Sens, vous pourrez ajouter 2 au chiffre que vous aurez tiré.'))
    roll = hazard_roll()
    if roll is not None:
        value = roll
        if has_kai("Le Sixième Sens"):
            value += 2
            st.write(f"*Sixième Sens : +2, total {value}.*")
        if value <= 4:
            st.write_stream(stream_text('Si vous obtenez un total de 0 à 4, rendez-vous au :'))
            st.page_link("tomes/tome3/page_22.py", label="22", icon="📄")
        else:
            st.write_stream(stream_text('Si votre total est de 5 à 11, rendez-vous au :'))
            st.page_link("tomes/tome3/page_326.py", label="326", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
