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

check_inventory(current_page_number=178, book=3)

fr_text = """
Vous suivez les éclaireurs Barbares depuis presque deux heures
lorsqu'un vent furieux et glacé se lève à l'ouest. Le terrain devient
très accidenté, et des amas de neige dissimulent des arêtes de
glace tranchantes comme des rasoirs ainsi que les inégalités du
sol qui risquent à tout moment de vous faire tomber. Grâce à
leurs skis (fabriqués à partir de côtes de mammouths de Kalte),
les éclaireurs Barbares n'ont aucune difficulté à parcourir cette
surface semée d'embûches. La traverser à pied représente
cependant une douloureuse épreuve. Le vent mordant balaie le
glacier et apporte avec lui des nuages déversant une neige fine
qui réduit sensiblement la visibilité. Vous prenez très vite
conscience du danger qu'il y aurait à être pris au milieu d'un
blizzard sur une étendue dépourvue de tout abri et vous faites
donc signe à vos compagnons d'abandonner la poursuite. Vous
vous dirigez vers eux lorsque, soudain, la glace se dérobe sous
vos pas, vous précipitant en de mystérieuses profondeurs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_105.py", label="105", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
