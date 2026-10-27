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

check_inventory(current_page_number=200, book=2)

fr_text = """
Lorsque vous arrivez au bar, tous les autres sont déjà assis à une grande
table et vous attendent. Vous vous approchez d'eux et, soudain, la vérité
vous apparaît clairement : vous savez à présent qui a tenté de vous
assassiner et vous décidez d'attaquer cet ennemi par surprise, sans le
laisser soupçonner que vous avez vu clair dans son jeu. Pendant
quelques instants, vous examinez attentivement le visage de vos
compagnons de voyage et vous avez alors la certitude d'avoir deviné
juste. Il ne vous reste plus qu'à passer à l'attaque. Mais qui est donc,
selon vous, cet assassin présumé sur lequel vous allez vous précipiter à
la seconde même ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Le Chevalier de la Montagne Blanche qui répond au nom de Dorier ? Rendez-vous au :"))
    st.page_link("tomes/tome2/page_7.py", label="7", icon="📄")

    st.write_stream(stream_text("Le marchand nommé Halvorc ? Rendez-vous au :"))
    st.page_link("tomes/tome2/page_60.py", label="60", icon="📄")

    st.write_stream(stream_text("Viveka l'aventurière ? Rendez-vous au :"))
    st.page_link("tomes/tome2/page_85.py", label="85", icon="📄")

    st.write_stream(stream_text("Le moine nommé Parsion ? Rendez-vous au :"))
    st.page_link("tomes/tome2/page_158.py", label="158", icon="📄")

    st.write_stream(stream_text("Le Chevalier de la Montagne Blanche qui se nomme Ganon ? Rendez-vous au :"))
    st.page_link("tomes/tome2/page_270.py", label="270", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
