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

check_inventory(current_page_number=150, book=7)

fr_text = """
Au début, gravir les marches branlantes, à moitié défoncées, ne
pose aucun problème à un Maître Kaï de votre qualité. Pourtant,
en arrivant près du sommet, vous vous trouvez confronté à une
difficulté de taille : une portion entière de l'escalier s'est
effondrée, laissant place à un vide de plus de six mètres de large.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de Nexus, et si vous souhaitez y avoir recours, rendez-vous au :"))
    if has_magnakai("Nexus"):
        st.page_link("tomes/tome7/page_255.py", label="255", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_255.py", label="255", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous possédez une Corde, rendez-vous au :"))
    st.page_link("tomes/tome7/page_310.py", label="310", icon="📄", disabled=not has_item("CORDE"))

    st.write_stream(stream_text("Si vous ne maîtrisez pas la Discipline de Nexus, et si vous n'avez pas de Corde, rendez-vous au :"))
    st.page_link("tomes/tome7/page_211.py", label="211", icon="📄", disabled=has_magnakai("Nexus") or has_item("CORDE"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
