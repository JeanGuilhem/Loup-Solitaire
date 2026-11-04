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

check_inventory(current_page_number=271, book=5)

fr_text = """
Le cavalier du Kraan passe en criant sur votre gauche, mais vous
réussissez à le dévier de sa trajectoire par une rapide contre-attaque.
Votre adversaire est à présent à plusieurs mètres en
dessous de vous, mais il fait effectuer à son Kraan un rapide
demi-tour pour passer de nouveau à l'attaque. Vous tournez vers
le sud pour éviter d'être pris entre les deux escadrons de Kraans
qui convergent vers vous. Votre brusque changement de
direction a augmenté la distance entre vous et vos poursuivants,
mais l'Itikar est grièvement blessé et, de plus, terrifié par les cris
stridents des Kraans. Vous perdez pratiquement tout espoir, car
votre monture perd beaucoup de sang et elle peut, d'un instant à
l'autre, sombrer dans l'inconscience et vous laisser tomber
comme une pierre dans le ciel obscurci. Soudain, vous apercevez
quelque chose dans le lointain : une vision qui vous fait croire
aux miracles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
