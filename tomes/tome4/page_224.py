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

check_inventory(current_page_number=224, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous entendez derrière vous le souffle rauque des Gardes.
Soudain le tunnel se rétrécit et bifurque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez emprunter le passage de gauche, rendez-vous au :'))
    st.page_link("tomes/tome4/page_199.py", label="199", icon="📄")

    st.write_stream(stream_text('Si vous préférez prendre celui de droite, rendez-vous au :'))
    st.page_link("tomes/tome4/page_208.py", label="208", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation ou celle du Sixième Sens, rendez-vous au :"))
    if has_kai("L'Orientation") or has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome4/page_60.py", label="60", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_60.py", label="60", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
