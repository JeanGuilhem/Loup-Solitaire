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

check_inventory(current_page_number=159, book=3)

fr_text = """
L'homme vous regarde droit dans les yeux et répond : « Le
Ragad. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez à présent effacer le pentagramme afin de le libérer, rendez-vous au :'))
    st.page_link("tomes/tome3/page_170.py", label="170", icon="📄")
    st.write_stream(stream_text('Si vous préférez vous en abstenir, refermez la porte de sa cellule et retournez dans le couloir principal en vous rendant au :'))
    st.page_link("tomes/tome3/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
