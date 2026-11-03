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

check_inventory(current_page_number=15, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous avez parcouru moins de 100 mètres, lorsque vous
remarquez des traces fraîches de sabots sur la poussière du
sentier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome4/page_264.py", label="264", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_264.py", label="264", icon="📄", disabled=True)

    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome4/page_134.py", label="134", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome4/page_134.py", label="134", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
