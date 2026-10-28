import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=291, book=3)

fr_text = """
Lorsque vous vous éveillez, vous sentez que quelque chose a
changé. Il vous faut alors presque une minute pour vous rendre
compte que le hurlement incessant du vent a cessé. « C'est une
belle matinée », dit Irian d'un ton joyeux, en passant la tête au-dehors.
Vous vous levez en hâte et vous allez jeter un coup d'œil à
l'extérieur. Devant vous, l'étendue de glace baigne dans un air
frais et limpide, et un mirage au loin semble projeter dans le ciel
le paysage de Kalte. « Nous devrions arriver au lieu dit Le Roc à
la nuit tombée, annonce Fenor en passant son harnais à un chien
Kanu récalcitrant. Nous ferions bien d'y établir notre camp
jusqu'à demain, c'est un bon abri. Sur la banquise, à cette
distance de la mer, un blizzard peut se lever à tout instant et tout
balayer sur son passage. Il est arrivé que des trappeurs
imprudents ou malchanceux soient ainsi emportés par les vents
sur des kilomètres après avoir été surpris à découvert. » Ce jour-là,
les traîneaux glissent sans difficulté à la surface lisse de la
banquise et les chiens peuvent avancer à bonne allure. Lorsque le
soir tombe, vous avez atteint Le Roc, comme prévu : il s'agit d'un
pic de granite qui s'élève à travers la glace et dont la forme
étrange vous rappelle la Citadelle du roi, à Holmgard, la capitale
de votre pays. Vous dressez votre tente à l'abri du Roc pour vous
protéger des vents nocturnes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    roll = hazard_roll()
    if roll is not None and roll <= 4:
        st.page_link("tomes/tome3/page_103.py", label="103", icon="📄")
    elif roll is not None:
        st.page_link("tomes/tome3/page_220.py", label="220", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
