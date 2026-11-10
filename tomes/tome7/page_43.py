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

check_inventory(current_page_number=43, book=7)

fr_text = """
Les Pilules Bleues sont faites de racine de Sabito séchée et
broyée. C'est une plante qu'on trouve en abondance dans la
jungle de Boari, mais qui est extrêmement rare dans les autres
contrées du Magnamund. Ces pilules permettent au corps
humain d'assimiler, par les pores de la peau, l'oxygène qui se
trouve dans l'eau. Ainsi, toute personne ayant absorbé de la
racine de Sabito peut aisément « respirer » sous l'eau. Dans le
flacon que vous venez de trouver, il y en a l'équivalent d'une
dose.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('A présent, rendez-vous au :'))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
