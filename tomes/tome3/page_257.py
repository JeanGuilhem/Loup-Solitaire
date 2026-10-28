import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=257, book=3)

fr_text = """
Un frisson vous parcourt l'échine tandis que les cris de Dyce
s'évanouissent à mesure qu'il tombe dans la gorge. Vous scrutez
encore l'obscurité du gouffre lorsqu'Irian s'écrie soudain: « Là !...
là-bas ! Je suis sûr que j'ai vu quelque chose. » Vous vous tournez
vers lui pour constater qu'il pointe l'index non pas vers le fond de
la gorge, mais en direction de l'ouest. « Regardez ! Là-bas ! » dit
à son tour Fenor qui montre une lointaine hauteur. Vous
apercevez alors deux guerriers vêtus de fourrure, debout au
sommet d'un gros bloc de glace. Ils regardent dans votre
direction, alertés sans nul doute par les hurlements de Dyce. « Ce
sont des Barbares des Glaces, murmure Irian, la voix tremblante
de peur. S'ils atteignent Ikaya avant nous, ils avertiront les autres
de notre présence et nous pourrons alors nous considérer comme
morts. » Il reste encore 25 kilomètres à parcourir pour atteindre
la Forteresse de Glace et, dans trois heures, la nuit sera tombée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez poursuivre votre chemin vers Ikaya en espérant arriver là-bas avant les Barbares, rendez-vous au :'))
    st.page_link("tomes/tome3/page_327.py", label="327", icon="📄")

    st.write_stream(stream_text("Si vous préférez les attaquer pour les empêcher de donner l'alerte, rendez-vous au :"))
    st.page_link("tomes/tome3/page_307.py", label="307", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
