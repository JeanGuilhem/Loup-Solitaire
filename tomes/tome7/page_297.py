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

check_inventory(current_page_number=297, book=7)

fr_text = """
Le martèlement incessant commence à produire son effet. (Vous
perdez 2 points d'ENDURANCE.) Vous savez que vous ne
pourrez pas longtemps résister à cet Assaut Psychique. Vous
devez absolument faire quelque chose pour l'arrêter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous avez une Graine de Feu et si vous souhaitez la jeter contre le socle, rendez-vous au :"))
    st.page_link("tomes/tome7/page_157.py", label="157", icon="📄", disabled=not (has_item("GRAINE DE FEU")))

    st.write_stream(stream_text("Si vous voulez courir vers le socle pour attaquer la main, rendez-vous au :"))
    st.page_link("tomes/tome7/page_116.py", label="116", icon="📄")

    st.write_stream(stream_text("Si vous préférez passer entre les deux piliers verts et pénétrer dans le tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_103.py", label="103", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
