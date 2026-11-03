import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=155, book=4)

fr_text = """
Derrière la meute des Chiens de Guerre, vous apercevez une
douzaine de brigands, armés d'arcs et de flèches, qui se
rapprochent. Même si vous parveniez à survivre à l'attaque des
Chiens de Guerre, ces archers auraient bientôt raison de vous. Il
ne vous reste donc plus qu'à prendre la fuite et vous vous mettez
à courir à toutes jambes en direction de Ruanon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_225.py", label="225", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
