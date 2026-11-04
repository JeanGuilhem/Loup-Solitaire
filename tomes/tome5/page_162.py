import streamlit as st
from combat import combat
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=162, book=5)

fr_text = """
Vous vous glissez dans le conduit de la cheminée de gauche et
vous faites une pause pour retrouver votre souffle. Les vapeurs
bouillantes vous brûlent les poumons et le moindre mouvement
vous demande d'énormes efforts, car vos mains enflées et votre
visage tuméfié vous font atrocement souffrir. Déduisez 1 point
d'ENDURANCE avant de reprendre votre escalade. Vous
remarquez une fissure dans le mur du conduit enfumé. Vous
l'utilisez comme prise et vous essayez de vous hisser le long de la
cheminée mais, soudain, effrayé à la vue de répugnants insectes
qui rampent sur vos bras, vous lâchez votre prise. Vous avez
dérangé un nid d'Araignées monstrueuses !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Ces créatures sont insensibles à la Puissance Psychique. Si vous avez perdu l'usage d'un de vos bras, vous ne pouvez combattre ces affreuses bestioles, sinon vous tomberiez immanquablement dans le tar-sorkh."))
    if has_flag("bras paralysé"):
        st.write_stream(stream_text("Dans ce cas, utilisez la Table de Hasard pour obtenir un chiffre. Le chiffre obtenu représente le nombre de points d'ENDURANCE que vous perdez au contact des Araignées (un 0 correspond à une perte de 10 points)."))
        roll = hazard_roll()
        if roll is not None:
            loss = roll if roll != 0 else 10
            if not st.session_state.get("visibility_araignees"):
                st.session_state["visibility_araignees"] = True
                change_endurance(-loss)
            st.metric(label="Endurance", value=st.session_state.endurance, delta=-loss)
            st.write_stream(stream_text("Si vous êtes toujours vivant après avoir dépassé le nid, rendez-vous au :"))
            st.page_link("tomes/tome5/page_114.py", label="114", icon="📄")
    else:
        outcome = combat([("ARAIGNÉES DES VAPEURS", 10, 35)], psychic_immune=True)
        if outcome == "win":
            st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
            st.page_link("tomes/tome5/page_114.py", label="114", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
