import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=10, book=3)

fr_text = """
Le sac contient quatre fioles de verre ouvragé. Elles sont remplies
de liquides rouge, orange, vert et noir. Lequel souhaitez-vous
examiner ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.page_link("tomes/tome3/page_90.py", label="Examiner la fiole rouge (90)", icon="🔴")
    st.page_link("tomes/tome3/page_171.py", label="Examiner la fiole orange (171)", icon="🟠")
    st.page_link("tomes/tome3/page_289.py", label="Examiner la fiole verte (289)", icon="🟢")
    st.page_link("tomes/tome3/page_225.py", label="Examiner la fiole noire (225)", icon="⚫")

    st.write_stream(stream_text('Vous pourrez utiliser ce sac comme Sac à Dos si vous en avez besoin.'))
    if not st.session_state.has_backpack:
        pickup_button("SAC À DOS", key="sac", label="Prendre le sac comme Sac à Dos")

    st.write_stream(
        stream_text(
            'Vous aurez le droit de quitter les lieux quand vous le souhaiterez et vous poursuivrez '
            'alors votre chemin vers le nord, le long du couloir, en vous rendant au :'
        )
    )
    st.page_link("tomes/tome3/page_126.py", label="126", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
