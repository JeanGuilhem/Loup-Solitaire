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

check_inventory(current_page_number=46, book=7)

fr_text = """
Le tunnel débouche sur une pièce hexagonale comportant deux
issues. Chacune d'elles est marquée par une arche en forme de
fer à cheval taillée dans un bloc de cristal étincelant. L'arche de
gauche est en rubis massif, celle de droite en jade.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez passer sous l'arche en rubis, rendez-vous au :"))
    st.page_link("tomes/tome7/page_349.py", label="349", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous engager sous l'arche en jade, rendez-vous au :"))
    st.page_link("tomes/tome7/page_163.py", label="163", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Invisibilité, de l'Exploration ou de l'Intuition, rendez-vous au :"))
    if has_magnakai("Invisibilité") or has_magnakai("Exploration") or has_magnakai("Intuition"):
        st.page_link("tomes/tome7/page_2.py", label="2", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_2.py", label="2", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
