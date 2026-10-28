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

check_inventory(current_page_number=52, book=3)

fr_text = """
Tandis que vous escaladez la rampe glissante, un craquement
derrière vous vous fait faire volte-face. L'entassement de
cristaux, au pied de la rampe, commence à bouger. Les cristaux
sont vivants ! D'un air incrédule, vous les voyez se transformer
en une masse d'anneaux translucides qui se déploient peu à peu,
révélant la forme d'une créature de glace. Le monstre glisse vers
vous en ondulant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez fuir cette créature en courant vers la porte de pierre, rendez-vous au :'))
    st.page_link("tomes/tome3/page_169.py", label="169", icon="📄")

    st.write_stream(stream_text('Si vous préférez la combattre, rendez-vous au :'))
    st.page_link("tomes/tome3/page_265.py", label="265", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
