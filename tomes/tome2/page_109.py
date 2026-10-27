import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=109, book=2)

fr_text = """
Vous battez des paupières pour chasser l'eau de vos yeux et vous
constatez alors que le vaisseau amiral de la flotte fantôme est en
flammes. Une fumée noire s'échappe de ses ponts et des langues de feu
orange et jaunes jaillissent de sa coque moisie. Hélas, vous n'avez
guère le loisir de contempler ce spectacle réconfortant ; soudain, en
effet, vous entendez un battement d'ailes au-dessus de votre tête : c'est
un Kraan qui fond sur vous en essayant de vous saisir entre ses serres
pointues. Il parvient à refermer ses griffes crochues sur l'étoffe de votre
cape et vous vous sentez aussitôt emporté dans les airs. Le vol
cependant est de courte durée, car vous dégainez le Glaive de Sommer
et vous en plongez la lame dans le ventre flasque de la créature. Avec
un cri de douleur, le Kraan lâche prise et vous retombez en priant le ciel
que votre chute ne soit pas trop douloureuse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_120.py", label="120", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
