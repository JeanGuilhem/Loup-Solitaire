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

check_inventory(current_page_number=184, book=2)

fr_text = """
Le Drakkarim rend l'âme à vos pieds et les pirates saisis de panique
s'enfuient à bord de leur bateau en train de sombrer ; voir un aussi
puissant guerrier ainsi terrassé leur a fait perdre tout courage. Le
capitaine Kelman rassemble aussitôt ses hommes et les lance à la
poursuite de l'ennemi en déroute. Les pirates sont jetés par-dessus bord
par les marins déchaînés. Le Sceptre Vert s'éloigne ensuite du vaisseau
pirate qui donne de la bande sur tribord. « Merci au nom de tout
l'équipage, Seigneur Kaï ! s'écrie alors le capitaine en vous serrant la
main. Nous sommes fiers et reconnaissants de vous avoir parmi nous. »
Une longue ovation retentit sur le pont : l'équipage tout entier vous rend
hommage en même temps que le capitaine. Vous aidez ensuite à
soigner les blessés tandis que l'on répare les dégâts subis à l'avant du
navire. Et une heure plus tard, le vent enfle à nouveau les voiles : vous
êtes reparti vers le royaume de Durenor.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
