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

check_inventory(current_page_number=112, book=7)

fr_text = """
La flèche transperce la sphère, puis disparaît complètement.
Craignant que votre projectile n'ait été totalement inefficace,
vous vous apprêtez à tirer une arme à main quand, soudain, il se
produit un éclair aveuglant suivi d'une énorme explosion. La
masse noire éclate en mille morceaux et se consume en une boule
de feu jaune. Une vague de chaleur intense vous brûle le visage
(vous perdez 1 point d'ENDURANCE), et, sous le choc de la
déflagration, vous êtes brutalement projeté à l'intérieur de la fissure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_16.py", label="16", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
