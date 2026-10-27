import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=326, book=2)

fr_text = """
Le capitaine ordonne à l'équipage de hisser toutes les voiles pour
essayer d'échapper aux pirates, mais le vaisseau de ces derniers est
rapide et ils s'efforcent de couper la route du Sceptre Vert. La collision
semble inévitable. « Attention à l'abordage ! » s'écrie le capitaine, alors
que le flanc du navire aux voiles rouges se dresse soudain devant vous.
Dans un fracas impressionnant, la proue du Sceptre Vert déchire le
flanc du bateau pirate. Des éclats de bois volent en tous sens et vous
êtes projeté à plat ventre sur le pont sous la violence du choc. Les
pirates montent immédiatement à l'assaut et vous apercevez avec
horreur, au milieu de cette horde vociférante, la silhouette vêtue de noir
d'un GUERRIER DRAKKARIM. Il vous a aussitôt repéré et s'avance
vers vous, son glaive impressionnant levé au-dessus de sa tête. Il vous
faut l'affronter dans un combat à mort.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER DRAKKARIM", 15, 25)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez la victoire, rendez-vous au :"))
        st.page_link("tomes/tome2/page_184.py", label="184", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
