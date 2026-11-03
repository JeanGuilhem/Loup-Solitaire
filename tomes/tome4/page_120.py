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

check_inventory(current_page_number=120, book=4)

fr_text = """
Après avoir chevauché pendant plusieurs heures, vous arrivez à
un croisement. Un grand panneau de signalisation indique deux
directions : Ruanon au sud, distante de 95 km ; Eshnar à l'est, à
65 km.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez prendre la direction du sud, rendez-vous au :'))
    st.page_link("tomes/tome4/page_33.py", label="33", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller à l'est, rendez-vous au :"))
    st.page_link("tomes/tome4/page_92.py", label="92", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
