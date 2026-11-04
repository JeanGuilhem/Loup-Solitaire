import streamlit as st
from combat import combat
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

check_inventory(current_page_number=244, book=5)

fr_text = """
Vous distinguez très nettement la route principale qui relie Chula
à la capitale. Elle franchit la longue plaine salée du lac Inrahim
par un viaduc haut de dix mètres. Ce viaduc est un excellent
point de repère grâce auquel vous pouvez vous orienter. La route
est bordée par des hameaux de petites maisons en pierre, aux
toits en terre battue. Au fur et à mesure que vous approchez de la
ville, leur nombre augmente et vous n'êtes plus qu'à sept
kilomètres de Chula lorsqu'un nuage sombre apparaît au-dessus
d'un de ces petits villages. C'est un nuage de Kraans ; et ceux-ci
font route pour vous intercepter. Brusquement, l'Itikar hurle de
douleur tandis qu'un paquet de plumes arrachées tombe en
tourbillonnant. Un des Kraans s'est approché et il se trouve
maintenant à moins de 100 mètres derrière vous. Son cavalier
Drakkar est en train de ranger une arbalète en bronze dans son
carquois et de tirer une longue épée noire. La flèche qu'il vient de
tirer a transpercé l'aile de votre monture et il s'apprête
maintenant à frapper avec son épée, alors que l'Itikar perd de la
hauteur et de la vitesse.
Le Kraan et son cavalier foncent sur vous ; le combat ne durera
qu'un seul Assaut car, emporté par son élan, le Drakkar ne
restera à votre niveau qu'un court instant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DRAKKAR", 20, 28)], key="drakkar", max_rounds=1)
    if outcome is not None:
        last = st.session_state["combat_drakkar"]["log"][-1]
        if last["ls_loss"] > last["enemy_loss"]:
            st.write_stream(stream_text("Si vous perdez plus de points d'ENDURANCE que votre adversaire au cours de cet unique Assaut, rendez-vous au :"))
            st.page_link("tomes/tome5/page_347.py", label="347", icon="📄")
        elif last["ls_loss"] < last["enemy_loss"]:
            st.write_stream(stream_text("Si votre adversaire perd plus de points d'ENDURANCE que vous, rendez-vous au :"))
            st.page_link("tomes/tome5/page_327.py", label="327", icon="📄")
        else:
            st.write_stream(stream_text("Si le nombre de points perdus est le même pour vous deux, rendez-vous au :"))
            st.page_link("tomes/tome5/page_271.py", label="271", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
