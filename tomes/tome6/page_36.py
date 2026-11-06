import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=36, book=6)

fr_text = """
Vous n'êtes plus qu'à quelques mètres du chariot quand soudain
votre cheval, refusant l'obstacle, s'arrête net et se cabre. La
longue chevauchée que vous lui avez imposée aujourd'hui lui a, en
effet, ôté toute force et toute envie d'accomplir un tel effort.
Vous êtes brusquement rejeté en arrière sur la croupe et vous
accrochez désespérément aux rênes tandis que l'animal piétine
maladroitement le sol de ses sabots postérieurs. Soudain, il fait
un faux pas et s'écroule en vous entraînant dans sa chute. Vous
êtes écrasé par le poids énorme de votre monture et, malgré tous
vos efforts pour vous en dégager, vous savez que la bataille est
perdue d'avance. Vos membres s'engourdissent peu à peu et une
douleur lancinante envahit votre cage thoracique à moitié
enfoncée. Votre aventure se termine, hélas ! ici.
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
