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

check_inventory(current_page_number=259, book=6)

fr_text = """
La porte, à moitié pourrie, n'a pas été ouverte depuis plus de
cent ans ! Si vous voulez savoir ce qu'il y a derrière, vous devez
nettoyer les gonds de la couche de rouille et de la saleté qui s'y
sont déposées.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de Nexus ou du Foudroiement Psychique, rendez-vous au :"))
    if has_magnakai("Nexus") or has_magnakai("Foudroiement Psychique"):
        st.page_link("tomes/tome6/page_186.py", label="186", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_186.py", label="186", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez aucune de ces disciplines, rendez-vous au :"))
    if not (has_magnakai("Nexus") or has_magnakai("Foudroiement Psychique")):
        st.page_link("tomes/tome6/page_156.py", label="156", icon="📄")
    else:
        st.page_link("tomes/tome6/page_156.py", label="156", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
