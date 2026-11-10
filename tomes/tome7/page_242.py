import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=242, book=7)

fr_text = """
Vous regardez par le trou de la serrure mais le pêne est enclenché
et vous ne voyez rien. L'eau vous arrive maintenant au menton,
submergeant complètement le verrou, et vous devez rester la tête
penchée en arrière pour pouvoir respirer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de Nexus, rendez-vous au :"))
    st.page_link("tomes/tome7/page_327.py", label="327", icon="📄", disabled=not (has_magnakai("Nexus")))
    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    st.page_link("tomes/tome7/page_153.py", label="153", icon="📄", disabled=has_magnakai("Nexus"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
