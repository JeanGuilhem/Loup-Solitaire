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

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=301, book=4)

fr_text = """
Vous passez bientôt devant des écuries bâties au milieu d'un
vaste enclos. De nombreux chevaux sont rassemblés là et chacun
d'eux est sellé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_kai("Communication Animale"):
        st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"))
        st.page_link("tomes/tome4/page_106.py", label="106", icon="📄")
    else:
        st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"))
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_106.py", label="106", icon="📄", disabled=True)
    st.write_stream(stream_text("Dans le cas contraire, rendez-vous au :"))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome4/page_236.py", label="236", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome4/page_236.py", label="236", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
