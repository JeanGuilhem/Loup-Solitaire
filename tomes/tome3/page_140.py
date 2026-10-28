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

check_inventory(current_page_number=140, book=3)

fr_text = """
L'enfant saisit soudain un couteau en os qu'il cachait dans sa
botte et vous enfonce la lame dans le dos de la main. Vous perdez
2 points d'ENDURANCE et vous lâchez le jeune garçon. Il court
aussitôt vers son père qui, à présent, a repris ses esprits et
dégaine une épée également en os dont la lame est incrustée de
dents redoutables.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_68.py", label="68", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
