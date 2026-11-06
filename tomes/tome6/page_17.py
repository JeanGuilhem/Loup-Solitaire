import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=17, book=6)

fr_text = """
Vous vous dirigez vers le comptoir et vous demandez une chambre
pour la nuit. Un tableau noir accroché en face de vous indique le
prix des chambres, selon la catégorie et le confort :

- Dortoir : 2 Pièces d'Or par nuit.
- Chambre Simple (2e classe) : 3 Pièces d'Or par nuit.
- Chambre Simple (1re classe) : 5 Pièces d'Or par nuit.

Vous pouvez choisir une chambre à votre convenance, sans oublier
de rayer sur votre Feuille d'Aventure les Pièces d'Or
correspondant au prix en vigueur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez passer la nuit dans le dortoir, rendez-vous au 144."))
    if st.button("Payer 2 Couronnes", key="room_144", disabled=st.session_state.purse < 2):
        spend_gold(2)
        st.switch_page("tomes/tome6/page_144.py")

    st.write_stream(stream_text("Si vous désirez prendre une chambre individuelle de seconde catégorie, rendez-vous au 202."))
    if st.button("Payer 3 Couronnes", key="room_202", disabled=st.session_state.purse < 3):
        spend_gold(3)
        st.switch_page("tomes/tome6/page_202.py")

    st.write_stream(stream_text("Si vous vous laissez tenter par une chambre de première classe, nettement plus confortable, avec bain, rendez-vous au 251."))
    if st.button("Payer 5 Couronnes", key="room_251", disabled=st.session_state.purse < 5):
        spend_gold(5)
        st.switch_page("tomes/tome6/page_251.py")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
