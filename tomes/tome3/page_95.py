import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=95, book=3)

fr_text = """
Le froid intense et les assauts incessants du cyclone épuisent très
vite vos réserves d'énergie. Un engourdissement inexorable vous
envahit tandis que le Démon de Glace prend possession de votre
corps, impatient de commencer une nouvelle existence au cours
de laquelle il exercera ses redoutables pouvoirs. Pour les
créatures d'Ikaya et bientôt du pays de Kalte tout entier, l'aube
vient de se lever sur un âge de tyrannie, une tyrannie terrifiante
et implacable dont vous ne verrez cependant jamais les effets, car
votre vie s'achève ici, en même temps, bien entendu, que votre
mission.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
