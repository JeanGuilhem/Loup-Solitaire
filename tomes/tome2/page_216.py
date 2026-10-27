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

check_inventory(current_page_number=216, book=2)

fr_text = """
Pendant trois jours et trois nuits, la puissante flotte du royaume de
Durenor file à bonne allure en direction du golfe de Holm ; un fort vent
gonfle les voiles des vaisseaux et il se pourrait bien que le voyage soit
plus court que prévu. Pourtant, le moral des soldats n'est pas au plus
haut ; il semble que leur confiance en eux-mêmes et leur hâte de
combattre se soient peu à peu évanouies, comme si quelque vampire
invisible les avait mystérieusement vidés de leur force. Lord Axim en
éprouve une grande contrariété. « Cette humeur sombre qui hante nos
navires est l'œuvre des Maîtres des Ténèbres, assure-t-il. Je connais
l'étendue de leur pouvoir lorsqu'il s'agit d'influencer l'esprit des
hommes, mais la malédiction qu'ils font peser sur nous est bien pire
encore, il est impossible de conjurer une telle sorcellerie. Je prie le ciel
que cette malédiction soit bientôt levée, car sinon, même si nous
arrivons à destination, nous n'aurons plus suffisamment de volonté pour
affronter l'ennemi. » Le lendemain à l'aube, la prière de Lord Axim
semble avoir été entendue. Le moral des hommes remonte en effet, et la
malédiction paraît avoir pris fin. Mais c'est désormais une autre menace
qui pèse sur la flotte de Durenor, une menace encore plus mortelle dont
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Vous en connaîtrez la nature en vous rendant au :'))
    st.page_link("tomes/tome2/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
