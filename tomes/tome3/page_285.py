import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=285, book=3)

fr_text = """
La porte s'ouvre en coulissant latéralement, et vous découvrez
avec horreur le regard d'un Barbare des Glaces qui vous fixe de
ses yeux blancs totalement dépourvus de pupilles. Un cri rauque,
qui ne ressemble à aucun son connu, monte de sa gorge et, un
instant plus tard, les Loups Maudits s'éveillent et se mettent à grogner.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous enfuir, il vous faut faire volte-face et redescendre l'escalier quatre à quatre ; rendez-vous alors au :"))
    st.page_link("tomes/tome3/page_261.py", label="261", icon="📄")

    st.write_stream(stream_text('Si vous préférez faire face et combattre, rendez-vous au :'))
    st.page_link("tomes/tome3/page_343.py", label="343", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
