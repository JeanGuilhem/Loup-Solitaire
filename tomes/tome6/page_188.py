import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=188, book=6)

fr_text = """
Le danger immédiat qui vous menace vous empêche de réfléchir
trop longuement aux raisons qui ont poussé ces cavaliers à
enlever Cyrilus. Néanmoins, il vous apparaît clairement que ni sa
santé ni ses talents de prestidigitateur ne justifient une rançon
élevée. Vous arrivez bientôt au pied du piton rocheux recouvert
d'arbres. La route continue tout droit avant de tourner
brusquement vers l'ouest. Juste après le tournant, vous
apercevez une église en pierre et son cimetière. Mais, à quelques
mètres devant vous, un homme jeune, le visage blême et balafré,
monté sur un destrier noir comme la nuit, vous bloque le
passage. Ses yeux froids et sombres vous dévisagent cruellement.
Vous le reconnaissez immédiatement : c'est Roark, le jeune
seigneur que vous avez battu à l'Auberge du Bout du Pont.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Broche en Argent, rendez-vous au :"))
    st.page_link("tomes/tome6/page_31.py", label="31", icon="📄", disabled=not (has_item("BROCHE EN ARGENT")))

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    st.page_link("tomes/tome6/page_14.py", label="14", icon="📄", disabled=has_item("BROCHE EN ARGENT"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
