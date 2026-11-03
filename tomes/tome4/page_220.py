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

check_inventory(current_page_number=220, book=4)

fr_text = """
Votre coup a désarçonné le brigand qui tombe lourdement sur le
sol en brisant sa lance dans sa chute. Il se remet sur pied avec
difficulté puis, relevant la visière de son heaume, il vous regarde
avec un sourire sardonique qui découvre deux rangées de dents
noires et pointues. Il laisse alors échapper son cri de guerre et se
précipite sur vous en dégainant un cimeterre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez combattre ce guerrier, rendez-vous au :'))
    st.page_link("tomes/tome4/page_90.py", label="90", icon="📄")

    st.write_stream(stream_text('Si vous préférez prendre la fuite, rendez-vous au :'))
    st.page_link("tomes/tome4/page_163.py", label="163", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
