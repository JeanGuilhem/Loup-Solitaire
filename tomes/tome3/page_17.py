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

check_inventory(current_page_number=17, book=3)

fr_text = """
Vous vous rendez compte que vous souffrez des premiers effets
de la cécité des neiges. A moins de réagir immédiatement,
d'autres symptômes plus douloureux de ce mal ne vont pas
tarder à se manifester.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            'Si vous souhaitez vous protéger les yeux par un bandeau que vous garderez au moins '
            "jusqu'au moment d'établir votre camp, plus tard dans la journée, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_62.py", label="62", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous n'aimez pas avoir un bandeau sur les yeux et que vous préfériez risquer la "
            'cécité des neiges, rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_251.py", label="251", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
