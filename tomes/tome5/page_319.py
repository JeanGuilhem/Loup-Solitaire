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

check_inventory(current_page_number=319, book=5)

fr_text = """
Le Médaillon d'Onyx commence à briller et à vibrer au fond de
votre poche. Cet Objet Spécial, que vous avez arraché de l'armure
d'un traître - un capitaine Vassagonien - lors de la bataille de
Ruanon, va vous permettre d'entrer en communication avec
l'Itikar. Vous faites comprendre à l'oiseau que vous ne lui voulez
aucun mal. Les Itikars sont des créatures sauvages et rusées de
nature mais, par son pouvoir, le Médaillon d'Onyx parvient à
dominer cette instinctive méfiance et à obtenir la docilité des
animaux envers celui qui le porte. Alors que vous vous installez
sur la confortable selle, vous voyez soudain des Drakkars
traverser la passerelle. Vous vous penchez pour délier la corde
qui retient l'Itikar par l'anneau de la selle et vous saisissez les
solides rênes de cuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_343.py", label="343", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
