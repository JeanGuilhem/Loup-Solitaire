import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=197, book=7)

fr_text = """
Utilisant au mieux les quelques possibilités de cachette qui vous
sont offertes, vous traversez la pièce tel un fantôme. Mais, dès
que vous pénétrez dans le couloir de l'autre côté, vous vous
retrouvez face à un garde en armure. Il pousse un cri étouffé par
la visière de son casque noir, puis fait demi-tour et court vers une
corde reliée à une cloche d'alarme, qui pend d'une ouverture
pratiquée dans le plafond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un arc et que vous souhaitiez l'utiliser, rendez-vous au :"))
    st.page_link("tomes/tome7/page_266.py", label="266", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous n'en possédez pas, ou que vous ne vouliez pas l'utiliser, rendez-vous au :"))
    st.page_link("tomes/tome7/page_40.py", label="40", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
