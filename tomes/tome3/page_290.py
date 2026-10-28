import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=290, book=3)

fr_text = """
La porte de pierre s'ouvre lentement, laissant apparaître une
arcade baignée de brume qui s'élève en volutes et vous empêche
de voir ce qui se trouve derrière. Vous remarquez alors que la
température a brutalement baissé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_kai("Le Sixième Sens") and kai_rank() >= 7:
        st.write_stream(stream_text('Vous maîtrisez la Discipline Kaï du Sixième Sens et vous avez atteint le rang de Gardien (7 Disciplines Kaï) : rendez-vous au :'))
        st.page_link("tomes/tome3/page_341.py", label="341", icon="📄")
    elif has_kai("Le Sixième Sens"):
        st.write_stream(stream_text("Vous maîtrisez la Discipline Kaï du Sixième Sens mais vous n'avez pas encore atteint le rang de Gardien : rendez-vous au :"))
        st.page_link("tomes/tome3/page_124.py", label="124", icon="📄")
    else:
        st.write_stream(stream_text("Vous ne maîtrisez pas la Discipline Kaï du Sixième Sens : vous vous préparez au combat et vous franchissez l'arcade baignée de brume. Rendez-vous au :"))
        st.page_link("tomes/tome3/page_264.py", label="264", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
