import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=247, book=6)

fr_text = """
La grand-route descend vers une large vallée qui porte les
marques de violents combats. Des maisons en ruine encore
fumantes bordent la route. Vous traversez un fleuve aux eaux
stagnantes par un vieux pont en bois tout branlant, puis vous
grimpez vers un bosquet d'arbres au sommet d'une petite butte.
A l'approche du sommet, vous entendez une sourde et lancinante
incantation s'élever des arbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez mettre pied à terre pour examiner le bosquet, rendez-vous au :"))
    st.page_link("tomes/tome6/page_13.py", label="13", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer votre route vers Soren, sans vous préoccuper de l'incantation, rendez-vous au :"))
    st.page_link("tomes/tome6/page_102.py", label="102", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome6/page_206.py", label="206", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_206.py", label="206", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
