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

check_inventory(current_page_number=235, book=3)

fr_text = """
Après avoir parcouru une courte distance, vous arrivez dans une
vaste grotte remplie de stalactites et de stalagmites. Le sol est
couvert de traces d'animaux et d'ossements, mais l'endroit
semble désert et tranquille.
Vous remarquez que le mur situé au nord présente une surface
lisse constituée de blocs de granit s'élevant jusqu'à un plafond
de glace, à plus de 30 mètres de hauteur. Soudain, vous
comprenez que vous êtes en train de contempler les fondations
de pierre d'Ikaya : vous avez donc enfin réussi à atteindre la
Forteresse de Glace. Vous distinguez alors, à demi cachée par un
entassement de cristal, une rampe qui mène à une grande porte
de pierre aménagée dans le mur de la forteresse. Cette
découverte vous donne un regain d'espoir : si vous parvenez, en
effet, à pénétrer dans la forteresse et à capturer rapidement
Vonotar, vous aurez encore le temps de revenir à l'endroit où est
ancré le Cardonal avant que les glaces d'hiver ne se forment sur
la mer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez traverser la caverne pour aller examiner la porte de pierre, rendez-vous au :"))
    st.page_link("tomes/tome3/page_52.py", label="52", icon="📄")
    st.write_stream(stream_text("Si vous préférez examiner les ossements répandus sur le sol, rendez-vous au :"))
    st.page_link("tomes/tome3/page_115.py", label="115", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
