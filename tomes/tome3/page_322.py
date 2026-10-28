import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=322, book=3)

fr_text = """
Tandis que vous courez sur la surface glissante, la glace
commence à se fissurer. En jetant un coup d'œil derrière vous,
vous constatez que le Languabarb s'est arrêté au bord du lac. Il
semble terrifié par l'ombre noire que vous aviez vu évoluer dans
l'eau. Or, cette ombre vient justement de réapparaître à moins de
5 mètres de vous. La panique vous saisit et vous vous mettez à
courir de plus en plus vite en priant le ciel que votre chance et la
glace tiennent bon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 2:
        st.write_stream(stream_text("Si vous tirez le 0, le 1 ou le 2, rendez-vous au :"))
        st.page_link("tomes/tome3/page_153.py", label="153", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text("Si vous tirez un chiffre de 3 à 9, rendez-vous au :"))
        st.page_link("tomes/tome3/page_59.py", label="59", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
