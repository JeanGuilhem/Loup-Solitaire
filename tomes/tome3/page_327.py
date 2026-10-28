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

check_inventory(current_page_number=327, book=3)

fr_text = """
A mesure que vous approchez d'Ikaya, votre récente rencontre
avec les Barbares des Glaces vous préoccupe de plus en plus.
Allez-vous réussir à arriver avant eux ou bien sont-ils déjà en
train de vous préparer une embuscade ? Irian et Fenor semblent
tous les deux très inquiets et vous ne dites pas grand-chose
tandis que vous parcourez ce trajet difficile. Vos soucis,
cependant, vous font oublier d'autres dangers plus familiers :
parvenu en effet à une douzaine de kilomètres de la forteresse, la
neige se dérobe soudain et vous êtes précipité dans une crevasse
que vous n'aviez pas vue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 8:
        st.write_stream(stream_text("Si vous tirez un chiffre de 0 à 8, rendez-vous au :"))
        st.page_link("tomes/tome3/page_105.py", label="105", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text("Si vous tirez le 9, rendez-vous au :"))
        st.page_link("tomes/tome3/page_144.py", label="144", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
