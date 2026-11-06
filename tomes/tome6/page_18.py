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

check_inventory(current_page_number=18, book=6)

fr_text = """
Des arcs mis à la disposition des concurrents sont disposés en
vrac, sur une grande table dressée au centre de la tente. La
plupart sont en triste état, mais vous finissez par en trouver
trois qui ne soient ni voilés ni fendus. L'un d'eux est un Jakan,
un arc vassagonien ; l'autre est un arc de Kalte, fait en os ; le
troisième est un arc de chasse du pays de Durenor.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous choisissez le Jakan, rendez-vous au :"))
    st.page_link("tomes/tome6/page_298.py", label="298", icon="📄")

    st.write_stream(stream_text("Si vous optez pour l'arc en os, rendez-vous au :"))
    st.page_link("tomes/tome6/page_214.py", label="214", icon="📄")

    st.write_stream(stream_text("Si vous préférez l'arc de chasse, rendez-vous au :"))
    st.page_link("tomes/tome6/page_60.py", label="60", icon="📄")

    st.write_stream(stream_text("Par ailleurs, si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, rendez-vous au :"))
    if has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_205.py", label="205", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_205.py", label="205", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
