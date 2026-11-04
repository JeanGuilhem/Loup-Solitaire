import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=22, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous souffrez d'une profonde blessure au poumon droit qui vous
fait perdre 8 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-8)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-8)

    st.write_stream(stream_text('Si vous êtes encore en vie, et si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :'))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_107.py", label="107", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_107.py", label="107", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous ne possédez pas cette Discipline, rendez-vous au :'))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_63.py", label="63", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_63.py", label="63", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
