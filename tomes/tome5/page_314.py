import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=314, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
« Vous trouverez Tipasa sur la Grand-Place. Il y est toujours à
cette heure-ci de la journée », dit la vieille femme en grimaçant
un sourire forcé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_358.py", label="358", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_358.py", label="358", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne maîtrisez pas cette Discipline, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_263.py", label="263", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_263.py", label="263", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
