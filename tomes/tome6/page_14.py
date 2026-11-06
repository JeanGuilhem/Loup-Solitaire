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

check_inventory(current_page_number=14, book=6)

fr_text = """
Soudain, les cavaliers surgissent et se déploient en demi-cercle
autour de vous. « Nous avons un petit compte à régler, homme du
Nord, siffle Roark, les lèvres retroussées dans un rictus
méprisant. Et j'exige d'être payé immédiatement. » Une brève lueur
de folie passe dans son regard tandis qu'il détache de son cou une
amulette qu'il brandit en l'air. « Viens, Tagazin, viens, je t'en
conjure ! Je te somme de sortir du Puits de la Douleur Éternelle
pour accourir vers moi ! » Cette odieuse incantation vous donne la
chair de poule et une certaine appréhension vous envahit. Vous
parcourez rapidement les alentours des yeux pour trouver une issue
et vous réalisez que la seule possibilité serait de passer par le
cimetière, entre Roark et ses hommes. Mais au moment précis où
vous lancez votre cheval sous le portail de pierre, une vision
d'horreur vous glace le sang.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_270.py", label="270", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
