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

check_inventory(current_page_number=69, book=6)

fr_text = """
Vous vous aplatissez dans l'étroit renfoncement en priant le
ciel que la créature passe sans vous voir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Invisibilité, ajoutez 5 au chiffre que vous avez tiré."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (5 if has_magnakai("Invisibilité") else 0)
        st.write(f"*Total : {total}.*")
        if total <= 5:
            st.write_stream(stream_text("Si le résultat est compris entre 0 et 5, rendez-vous au :"))
            st.page_link("tomes/tome6/page_128.py", label="128", icon="📄")
        else:
            st.write_stream(stream_text("S'il est compris entre 6 et 14, rendez-vous au :"))
            st.page_link("tomes/tome6/page_246.py", label="246", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
