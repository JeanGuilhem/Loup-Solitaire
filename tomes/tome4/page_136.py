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

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=136, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
L'homme blessé est en état de choc. Son bras gauche est
complètement écrasé au-dessus et au-dessous du coude, et il a
plusieurs côtes cassées.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :'))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome4/page_313.py", label="313", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_313.py", label="313", icon="📄", disabled=True)

    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    st.page_link("tomes/tome4/page_216.py", label="216", icon="📄", disabled=has_kai("La Guérison"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
