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

check_inventory(current_page_number=14, book=7)

fr_text = """
La brique s'enfonce, et la porte dérobée s'ouvre en coulissant
silencieusement. Devant vous se tient un affreux nain barbu, vêtu
d'un habit en velours noir d'aspect crasseux. Ses petits yeux
porcins s'animent d'une lueur malveillante tandis qu'il pointe sur
vous un curieux tube en bronze. « Faites de beaux rêves ! »
l'entendez-vous dire. Simultanément, un jet de vapeur glaciale
jaillit de la gueule du tube et vous atteint en pleine figure. Vous
reculez en titubant, à demi suffoqué par la vapeur froide et acide
qui vous brûle les poumons. Le temps que vous réalisiez ce qui
vous arrive, vous succombez au puissant pouvoir narcotique de
ce gaz.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome7/page_165.py", label="165", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
