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

check_inventory(current_page_number=34, book=5)

fr_text = """
En dépit de tous vos efforts, l'image mentale du mécanisme ne se
forme pas. La fatigue psychique due à cet effort de concentration
vous fait perdre 1 point d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text('Si vous voulez tenter de fracturer la porte, rendez-vous au :'))
    st.page_link("tomes/tome5/page_127.py", label="127", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous éloigner et vous diriger à présent vers l'autre passage menant à l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_93.py", label="93", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
