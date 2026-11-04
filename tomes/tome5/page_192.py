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

check_inventory(current_page_number=192, book=5)

fr_text = """
La chaleur devient de plus en plus accablante. Par trois fois, vous
glissez et vous manquez de perdre l'équilibre, mais grâce à vos
bons réflexes, vous échappez à une mort cruelle dans le tar-
sorkh. Vous réussissez à grimper quelques mètres, mais à quel
prix ! Vos doigts et vos genoux, qui sont écorchés à vif, saignent
abondamment et vos jambes vous font très mal. Vous perdez 2
points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_114.py", label="114", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
