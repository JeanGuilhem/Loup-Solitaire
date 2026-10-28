import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=262, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
L'enfant vous donne des coups de pied et vous mord en se
débattant comme un animal sauvage. Utilisez la Table de Hasard
pour obtenir un chiffre qui vous indiquera si vous allez parvenir à
le maîtriser.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 6:
        st.page_link("tomes/tome3/page_320.py", label="320", icon="📄")
    elif roll is not None:
        st.page_link("tomes/tome3/page_140.py", label="140", icon="📄")

    st.write_stream(stream_text('Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai('Le Sixième Sens'):
        st.page_link("tomes/tome3/page_71.py", label="71", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_71.py", label="71", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
