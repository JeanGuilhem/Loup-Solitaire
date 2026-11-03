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

check_inventory(current_page_number=215, book=4)

fr_text = """
Une odeur de mort et de décomposition flotte autour de Barraka.
Chaussé de bottes qui lui montent jusqu'aux genoux, un long
cimeterre accroché à la ceinture, il pénètre dans le temple en
claquant derrière lui une lourde porte de pierre, d'un geste
désinvolte révélant une force hors du commun. Il reste un instant
immobile puis ouvre les deux grandes portes noires gravées de
têtes de morts. Soudain, une violente rafale de vent s'engouffre
dans le temple et un terrible hurlement retentit à vos oreilles.
Derrière les portes ouvertes, un surplomb rocheux projette sa
silhouette dans l'abîme des gorges de Maaken : vous êtes en train
de contempler le gouffre maudit. Barraka se détourne des portes
et marche lentement vers l'autel. D'un fourreau caché sous ses
vêtements, il tire alors un poignard noir à la lame ondulée. Il le
brandit dans la lumière et une flamme bleue jaillit aussitôt le
long de la lame d'acier. Les vents glacés des gorges de Maaken
font vaciller la flamme maléfique. Le sacrifice est sur le point de
s'accomplir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez attaquer Barraka, rendez-vous au :'))
    st.page_link("tomes/tome4/page_296.py", label="296", icon="📄")

    st.write_stream(stream_text("Si vous préférez distraire son attention sans l'attaquer, rendez-vous au :"))
    st.page_link("tomes/tome4/page_119.py", label="119", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
