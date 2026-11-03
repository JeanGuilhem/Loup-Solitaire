import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=275, book=4)

fr_text = """
D'un seul coup de votre épée d'or, vous brisez le pilier de bois.
Un tremblement agite le sol et, dans un grondement
assourdissant, un déluge de terre et de pierres se déverse dans le
tunnel, bloquant complètement le passage. Vous êtes aussitôt
enveloppé d'un nuage de fumée. Toutes les Torches se sont
éteintes et, sous la violence du choc, vous avez été projeté à terre
dans une chute qui vous fait perdre 1 point d'ENDURANCE.
Vous vous relevez à grand-peine et vous vous mettez à courir le
long du tunnel envahi de poussière, en direction d'une lointaine
clarté diffusée par des Torches que le choc de l'éboulement n'a
pas soufflées.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_335.py", label="335", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
