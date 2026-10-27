import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=29, book=2)

fr_text = """
Vous soulevez le loquet et vous faites glisser le panneau de l'écoutille.
L'ouverture provoque un brusque appel d'air et des flammes jaillissent
aussitôt de la cale. Vous reculez en titubant et en tenant à deux mains
votre visage brûlé par le feu. Vous perdez 2 points d'ENDURANCE.
« Au feu ! Au feu ! » crie alors une voix. L'équipage saisi de panique
s'efforce d'éteindre les flammes mais il faut plus d'une heure pour venir
à bout de l'incendie. Les dégâts sont considérables : c'est en effet dans
la cale qui a pris feu qu'étaient entreposées les réserves d'eau douce et
les vivres ; il n'en reste plus rien désormais. Mais, peut-être plus grave
encore, l'incendie a sérieusement endommagé la structure même du
navire. Tandis que vous examinez les dégâts, le capitaine s'approche de
vous, le visage noirci par la fumée. Il porte un paquet sous son bras. « Il
faut que je vous parle en privé, my lord », dit-il à voix basse. Sans rien
répondre, vous vous tournez vers lui et vous le suivez jusqu'à sa cabine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_222.py", label="222", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
