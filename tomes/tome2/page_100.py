import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=100, book=2)

fr_text = """
Un voile de brume s'est répandu sur la mer calme. Il vient des îles
Kirlundin, un archipel rocheux situé au nord-est du Sommerlund. Des
formes étranges et sombres apparaissent bientôt dans le brouillard ;
elles grandissent peu à peu et quelques minutes plus tard, on parvient à
en distinguer plus nettement les contours : ce sont des navires. «
Branle-bas de combat ! » crie aussitôt l'amiral et son ordre est répété
comme en écho sur tous les navires de la flotte de Durenor. « Tout le
monde sur le pont ! » A mesure que les bateaux ennemis s'approchent
dans le brouillard, un spectacle terrifiant vous frappe de stupeur : ce
sont en effet des vaisseaux fantômes qui s'avancent vers vous, des
épaves menées par les cadavres vivants de marins péris en mer. Et ces
navires renfloués par quelque effrayant prodige de haute sorcellerie se
préparent à combattre la flotte de Durenor. Soudain, la brume se dissipe
et vous voyez distinctement les bateaux fantômes se disposer en ligne
pour interdire l'entrée du golfe de Holm. Le vaisseau amiral de cette
flotte maléfique a pris place au milieu de la rangée et fait voile vers
vous, son rostre immense pointant à l'extrémité de sa proue noire. Un
instant plus tard, le puissant éperon déchire la coque du Durenor et
vous entendez la voix désespérée de l'amiral lancer un ordre : « Sauve
qui peut ! Abandonnez le navire ! » Le Durenor à présent est encerclé
par la flotte ennemie et sombre rapidement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez sauter sur le pont du vaisseau amiral de la flotte fantôme, rendez-vous "
            "au :"
        )
    )
    st.page_link("tomes/tome2/page_30.py", label="30", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez plonger dans la mer et tenter de gagner à la nage un autre navire de la "
            "flotte de Durenor, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
