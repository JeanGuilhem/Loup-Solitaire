import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=292, book=2)

fr_text = """
Vous marchez sous la pluie depuis trois bonnes heures lorsque vous
rencontrez soudain sept hommes à cheval qui vous barrent le passage.
Ce sont des mercenaires au service du Suzerain de Ragadorn dont ils
arborent l'emblème gravé sur leurs écussons : un vaisseau noir
surmonté d'une crête rouge. Ils vous ordonnent de leur donner tout
votre or, sinon, ils vous tueront sur place ; et lorsqu'ils s'aperçoivent
que vous n'avez plus la moindre Couronne dans votre bourse, vous avez
beau essayer de prendre la fuite, ils ont tôt fait de vous rattraper et de
vous tailler en pièces. Alors, tandis que vous agonisez sur le bord de la
route, les contours de Ragadorn se dessinent au loin : c'est la dernière
vision que vous emporterez de ce monde car, un instant plus tard, vos
yeux se ferment à jamais. Votre mission s'achève donc ici, en même
temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
