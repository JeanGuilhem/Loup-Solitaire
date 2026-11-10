import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
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

check_inventory(current_page_number=68, book=7)

fr_text = """
L'épée qui se trouve devant vous semble tout à fait normale, mais
le bloc de marbre sur lequel elle repose dégage, en revanche, une
forte aura de sorcellerie. Votre instinct Kaï vous déconseille de
vous en approcher de trop près.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de Nexus, rendez-vous au :"))
    if has_magnakai("Nexus"):
        st.page_link("tomes/tome7/page_124.py", label="124", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_124.py", label="124", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous possédez une Corde et si vous voulez tenter d'attraper l'épée au lasso, rendez-vous au :"))
    st.page_link("tomes/tome7/page_182.py", label="182", icon="📄", disabled=not (has_item("CORDE")))

    st.write_stream(stream_text("Si cette arme ne vous intéresse pas, vous pouvez quitter la cave par le tunnel de gauche, rendez-vous dans ce cas au :"))
    st.page_link("tomes/tome7/page_298.py", label="298", icon="📄")

    st.write_stream(stream_text("Ou bien par le tunnel de droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
