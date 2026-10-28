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

check_inventory(current_page_number=209, book=3)

fr_text = """
Vous vous cramponnez à la paroi rocheuse pendant toute la nuit.
Le vent glacial vous cingle le visage et vous êtes saisi de
tremblements incontrôlables, luttant de toutes vos forces pour ne
pas vous évanouir. Vous perdez 2 points d'ENDURANCE. L'huile
de Bakanal vous permet cependant de conserver suffisamment
de chaleur dans votre corps pour arriver à survivre : sans elle, le
froid aurait eu raison de vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text("Rendez-vous à présent au :"))
    st.page_link("tomes/tome3/page_155.py", label="155", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
