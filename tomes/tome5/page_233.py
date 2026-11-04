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

check_inventory(current_page_number=233, book=5)

fr_text = """
En plaçant le Prisme au centre du rayon, vous dirigez la lumière
vers le trou creusé dans le sol. Vous entendez les dalles de pierre
frotter l'une contre l'autre, puis vous voyez la porte s'ouvrir
lentement sur une grande pièce. Cette pièce est faiblement
éclairée, mais vous voyez se dessiner, dans la poussière qui
recouvre le sol de marbre, d'innombrables traces de pas. Tandis
que vous entrez, vous apercevez tout à coup un trône en pierre
brute qui fait face au mur du fond de la pièce. Derrière vous, la
porte se referme silencieusement à une vitesse déconcertante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_289.py", label="289", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
