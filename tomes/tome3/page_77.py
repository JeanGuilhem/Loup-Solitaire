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
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=77, book=3)

fr_text = """
Vous reconnaissez l'odeur âcre de Ronces des Cimetières que l'on
a distillées. C'est là un poison violent et les simples vapeurs qui
s'en dégagent sont suffisantes pour vous faire tourner la tête et
vous troubler la vue. Vous vous hâtez de vous débarrasser du
verre cassé et vous vous couvrez le nez avec la manche de votre
tunique. Les vapeurs empoisonnées vous font perdre 1 point
d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text('Retournez au 10 pour faire un autre choix :'))
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
