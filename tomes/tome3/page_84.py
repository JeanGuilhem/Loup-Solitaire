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

check_inventory(current_page_number=84, book=3)

fr_text = """
Vous remarquez que le Languabarb porte au cou un Triangle de
Pierre Bleue accroché à une chaînette et vous comprenez tout à
coup à quoi sert cette amulette. Vous vous en emparez, vous vous
précipitez vers la porte de la forteresse et vous appliquez l'objet
sur le triangle gravé dans le mur. L'amulette s'y encastre
exactement. Le rebord sur lequel vous vous tenez se met alors à
vibrer et vous entendez le grincement de pierres qui frottent
l'une contre l'autre. La porte s'ouvre, mais à peine s'est-elle
entrebâillée d'un mètre qu'un craquement retentit : elle
commence alors à se refermer. Sans hésiter une seconde, vous
plongez à l'intérieur de la forteresse ; un instant plus tard, la
lourde porte claque derrière vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
