import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=32, book=2)

fr_text = """
Le chant d'un coq vous réveille à l'aube. Les rues sinueuses de
Ragadorn vous apparaissent alors derrière un voile de pluie, une pluie
régulière et abondante qui martèle le pavé. Il y a six jours que vous
avez quitté Holmgard et il vous reste 320 kilomètres à parcourir avant
d'atteindre Port Bax. Vous êtes couché dans le grenier d'un vaste relais
de diligence. Un groupe d'hommes vêtus d'uniformes verts vient
d'arriver ; ils sont en train de nettoyer l'une des diligences. Vous
entendez une voix dire que le prochain départ pour Port Bax aura lieu à
une heure de l'après-midi et que le voyage durera sept jours. Vous avez
faim et il vous faut prendre un Repas, sinon, vous perdrez 3 points
d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()
    st.write_stream(stream_text("Après avoir mangé, vous déciderez peut-être d'acheter un billet pour Port Bax aux employés de la diligence ; dans ce cas, rendez-vous au :"))
    st.page_link("tomes/tome2/page_136.py", label="136", icon="📄")
    st.write_stream(stream_text("Mais vous pouvez également quitter le relais en empruntant l'échelle extérieure qui vous permettra de descendre directement dans la rue ; rendez-vous alors au :"))
    st.page_link("tomes/tome2/page_238.py", label="238", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
