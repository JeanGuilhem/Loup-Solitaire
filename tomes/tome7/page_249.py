import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=249, book=7)

fr_text = """
Les créatures se rapprochent en poussant des gloussements de
délectation. Des griffes jaillissent à l'extrémité des doigts de leurs
mains palmées et tannées comme du cuir tandis qu'elles
s'apprêtent à vous sauter dessus, le regard féroce brillant d'une
lueur rouge.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez vous enfuir en courant vers l'entrée du tunnel opposé, après le troisième Assaut."))
    outcome = combat([("DHAX", 27, 35)], flee_after=3)
    if outcome == "fled":
        st.write_stream(stream_text("Vous vous enfuyez vers l'entrée du tunnel opposé. Rendez-vous au :"))
        st.page_link("tomes/tome7/page_241.py", label="241", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_141.py", label="141", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
