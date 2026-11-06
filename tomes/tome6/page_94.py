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

check_inventory(current_page_number=94, book=6)

fr_text = """
Ecartant le rideau d'une main, vous pénétrez dans une petite
pièce encombrée d'établis et de placards. Vous parcourez des
yeux l'arrière-boutique, mais il n'y a plus aucune trace de
l'homme: il s'est littéralement volatilisé !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition ou de l'Art de la Chasse, rendez-vous au :"))
    if has_magnakai("Intuition") or has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_208.py", label="208", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_208.py", label="208", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez aucune de ces Disciplines, rendez-vous au :"))
    if has_magnakai("Intuition") or has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_37.py", label="37", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_37.py", label="37", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
