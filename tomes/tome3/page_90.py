import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=90, book=3)

fr_text = """
Après avoir essuyé le bouchon de la fiole, vous le dévissez et vous
reniflez avec prudence le liquide rouge.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :'))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome3/page_233.py", label="233", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_233.py", label="233", icon="📄", disabled=True)

    st.write_stream(stream_text('Dans le cas contraire, vous vous méfiez des effets peut-être nocifs de ce liquide et vous vous en débarrassez. Retournez au 10 pour faire un nouveau choix :'))
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄", disabled=has_kai("La Guérison"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
