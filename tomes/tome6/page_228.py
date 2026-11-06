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

check_inventory(current_page_number=228, book=6)

fr_text = """
Le vin a un bouquet délicieux et une belle robe. L'homme doit
vous tenir en haute estime car un vin tel que celui-ci est
sûrement rare et très cher.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, rendez-vous au :"))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome6/page_136.py", label="136", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_136.py", label="136", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, buvez votre verre de vin et rendez-vous au :"))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome6/page_84.py", label="84", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_84.py", label="84", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
