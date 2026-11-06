import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=278, book=6)

fr_text = """
Vous tournez la tête et apercevez une horrible créature qui émerge
lentement des ténèbres. Elle s'avance vers vous en poussant des
râles affreux et, brusquement, elle attaque. Elle vous donne un
violent coup de patte et vous tombez à la renverse sur les dalles
recouvertes de boue. Vous vous relevez rapidement, mais ses
griffes acérées se sont enfoncées profondément dans votre bras
vous faisant perdre 3 points d'ENDURANCE. La créature passe de
nouveau à l'attaque, les yeux brillant de haine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text("Si vous possédez un Arc, rendez-vous au :"))
    if has_item("ARC"):
        st.page_link("tomes/tome6/page_198.py", label="198", icon="📄")
    else:
        st.page_link("tomes/tome6/page_198.py", label="198", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'en possédez pas, rendez-vous au :"))
    if not has_item("ARC"):
        st.page_link("tomes/tome6/page_343.py", label="343", icon="📄")
    else:
        st.page_link("tomes/tome6/page_343.py", label="343", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
