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

check_inventory(current_page_number=321, book=6)

fr_text = """
Vous brandissez le Glaive de Sommer en tremblant. Votre arme
neutralise le pouvoir de la Baguette d'or du chef. Vous faites
tourner le Glaive au-dessus de votre tête et renvoyez l'éclair
d'énergie dans sa direction. La fureur du chef disparaît et il
blêmit de peur. Il reçoit la décharge en plein visage et se
désintègre, consommé dans une boule de feu d'une blancheur
aveuglante. Mais tandis que vous avancez, vous remarquez que
chaque participant possède une Baguette d'or. Dans un
mouvement d'ensemble, ils brandissent leurs Baguettes, unissant
leur pouvoir pour tenter de détruire votre épée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez poursuivre votre attaque, rendez-vous au :'))
    st.page_link("tomes/tome6/page_257.py", label="257", icon="📄")

    st.write_stream(stream_text('Si vous préférez prendre la fuite, rendez-vous au :'))
    st.page_link("tomes/tome6/page_182.py", label="182", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
