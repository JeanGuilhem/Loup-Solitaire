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

check_inventory(current_page_number=53, book=7)

fr_text = """
La douleur devient rapidement insupportable. (Vous perdez 5
points d'ENDURANCE.) Tandis que vous reculez en chancelant,
le rythme du martèlement s'accélère ; si vous ne réagissez pas
immédiatement, il détruira votre cerveau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-5)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-5)

    st.write_stream(stream_text("Si vous voulez attaquer la main, rendez-vous au :"))
    st.page_link("tomes/tome7/page_136.py", label="136", icon="📄")

    st.write_stream(stream_text("Si vous possédez une Graine de Feu et que vous voulez la lancer sur le socle où repose la main, rendez-vous au :"))
    st.page_link("tomes/tome7/page_157.py", label="157", icon="📄", disabled=not (has_item("GRAINE DE FEU")))

    st.write_stream(stream_text("Si vous préférez vous élancer entre les deux grands piliers verts et fuir par le passage qui continue au-delà, rendez-vous au :"))
    st.page_link("tomes/tome7/page_103.py", label="103", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
