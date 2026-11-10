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

check_inventory(current_page_number=113, book=7)

fr_text = """
Le grincement de la porte tire l'homme de son sommeil, et il se
recroqueville instinctivement dans un coin de la cage puante. Ses
yeux sont vitreux et son visage, ainsi que ses mains, portent les
stigmates de la maladie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, rendez-vous au :"))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome7/page_192.py", label="192", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_192.py", label="192", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette discipline, rendez-vous au :"))
    st.page_link("tomes/tome7/page_247.py", label="247", icon="📄", disabled=has_magnakai("Science Médicale"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
