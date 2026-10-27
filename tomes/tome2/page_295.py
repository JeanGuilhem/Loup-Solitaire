import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=295, book=2)

fr_text = """
L'une des créatures, plus grande que les autres et vêtue d'une
magnifique robe de soie en patchwork, crie un ordre dans son étrange
dialecte. Tous ses congénères saisissent alors des lances et des épées
qui semblent avoir été taillées dans les rayons d'une roue de chariot ou
dans des manches à balai. Puis ils se précipitent sur vous en poussant
de curieux cris de guerre, quelque chose comme « Gashiss, Nashiss».
Vous n'avez cependant pas le temps de vous intéresser à leur langage,
car bientôt vous serez piétiné à mort par une véritable armée de ces
petits êtres hargneux, si vous ne prenez pas immédiatement la fuite.
Vous faites donc volte-face et vous courez à perdre haleine le long d'un
couloir étroit, jusqu'à ce que leurs cris ne soient plus derrière vous
qu'une faible rumeur. Quelques instants plus tard, vous parvenez au
bout du passage qui débouche sur le tunnel principal. Vous pouvez
à présent continuer votre chemin à une allure plus tranquille.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_340.py", label="340", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
