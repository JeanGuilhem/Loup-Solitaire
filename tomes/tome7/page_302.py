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

check_inventory(current_page_number=302, book=7)

fr_text = """
Au moment où vous vous approchez du socle, les doigts de la
main commencent à bouger. Ils se lèvent et retombent sur la
surface granitique en battant un rythme lent et sourd. Ce
martèlement résonne dans votre tête, et vous ressentez une
douleur lancinante qui augmente un peu plus à chaque
battement des doigts noirs et gonflés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Écran Psychique, rendez-vous au :"))
    if has_magnakai("Écran Psychique"):
        st.page_link("tomes/tome7/page_179.py", label="179", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_179.py", label="179", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    st.page_link("tomes/tome7/page_53.py", label="53", icon="📄", disabled=has_magnakai("Écran Psychique"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
