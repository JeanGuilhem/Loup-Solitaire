import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=166, book=5)

fr_text = """
Vous massez votre bras endolori dans l'espoir de lui redonner un
peu de vie, mais tout effort est inutile : il est complètement
paralysé. Votre seule consolation vient du fait que ce n'est pas le
bras qui manie les armes, mais celui qui tient le bouclier. Étant
donné que vous ne pouvez plus vous protéger, ôtez 3 points à
votre total d'HABILETÉ. Ces points pourront être récupérés
ultérieurement si vous retrouvez l'usage de votre bras. Vous
examinez attentivement les environs afin de trouver un moyen
quelconque de fuir cet égout cauchemardesque. Le souterrain qui
s'ouvre devant vous tourne et vire comme un gigantesque
serpent et un vent chaud et humide d'air vicié souffle dans votre
direction. Vous avez semé vos poursuivants, mais il vous reste à
résoudre le problème de votre bras.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.session_state.hability -= 3
        set_flag("bras paralysé")
    st.metric(label="Habileté", value=st.session_state.hability, delta=-3)
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_55.py", label="55", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
