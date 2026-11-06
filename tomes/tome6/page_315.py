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

check_inventory(current_page_number=315, book=6)

fr_text = """
Lorsque les cris horribles du chef parviennent à vos oreilles, vous
ressentez une douleur atroce qui vous vrille les tempes. Vous êtes
attaqué par une puissante Force Psychique qui vous fait perdre 4
points d'ENDURANCE. Les membres de la secte se délectent de
vos souffrances, vos cris de douleur semblent résonner à leurs
oreilles comme la plus douce des musiques. Ils s'avancent
maintenant vers vous en tirant des poignards dissimulés sous
leur robe de bure et tentent de vous encercler. Rassemblant vos
dernières forces, vous faites demi-tour et partez au galop en
essayant de mettre entre vous et ce danger le plus de distance
possible.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
