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

check_inventory(current_page_number=153, book=7)

fr_text = """
Les eaux ont encore monté, et vous flottez maintenant au ras de
la brume tourbillonnante qui envahit le plafond de la chambre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer de fuir en vous enfonçant dans la brume, rendez-vous au :"))
    st.page_link("tomes/tome7/page_60.py", label="60", icon="📄")

    st.write_stream(stream_text("Si vous préférez plonger pour aller examiner la statue, rendez-vous au :"))
    st.page_link("tomes/tome7/page_168.py", label="168", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome7/page_307.py", label="307", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_307.py", label="307", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
