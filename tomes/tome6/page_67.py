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

check_inventory(current_page_number=67, book=6)

fr_text = """
Un silence de mort s'abat sur la ruelle tandis que des regards
accusateurs se posent sur vous. Le visage déformé par la haine,
le chef de la secte pointe un doigt crochu vers vous, tout en
marmottant une odieuse malédiction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Écran Psychique, rendez-vous au :"))
    if has_magnakai("Écran Psychique"):
        st.page_link("tomes/tome6/page_255.py", label="255", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_255.py", label="255", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette discipline, rendez-vous au :"))
    if has_magnakai("Écran Psychique"):
        st.page_link("tomes/tome6/page_315.py", label="315", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_315.py", label="315", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
