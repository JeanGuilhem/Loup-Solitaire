import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=16, book=2)

fr_text = """
Vous saisissez un verre de bière et vous le fracassez contre le bord de la
table. L'éclat de verre que vous tenez à présent entre vos doigts est
coupant comme un rasoir. Vous en passez le tranchant sur le dos de
votre main gauche et une longue estafilade apparaît aussitôt d'où
s'écoule un mince filet de sang. Vous pressez ensuite la paume de votre
main droite contre la blessure et vous vous concentrez. Une douceur
tiède se répand alors sur votre main blessée tandis que votre pouvoir
guérit la plaie. Lorsque vous ôtez votre main droite, il ne reste plus
trace de la coupure, pas même la plus petite cicatrice. Le marin vous
observe d'un air stupéfait.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_268.py", label="268", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
