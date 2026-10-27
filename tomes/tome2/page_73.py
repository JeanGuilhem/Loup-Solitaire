import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=73, book=2)

fr_text = """
L'escalade se révèle malaisée car vous n'avez qu'une seule main libre,
l'autre tenant le pommeau du Glaive de Sommer. Finalement, vous
parvenez quand même au sommet de la tour et vous vous hâtez
d'enjamber le muret qui tient lieu de garde-fou. Vous vous apprêtez à
sauter à l'intérieur de la tour et à passer à l'attaque lorsqu'une petite voix
vous fige sur place : « Votre mort sera pour moi un spectacle tout à fait
délectable, Loup Solitaire. » Vous apercevez alors le sorcier qui se tient
dans le coin opposé de la tour, sa main gauche tendue vers vous. «
Votre Mission a échoué, Loup Solitaire, dit-il ; à présent, il faut songer
à mourir. » Un éclair s'échappe aussitôt de sa main et une flamme
orange jaillit en direction de votre visage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_336.py", label="336", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
