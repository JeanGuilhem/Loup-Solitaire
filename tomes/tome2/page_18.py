import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=18, book=2)

fr_text = """
Un peu plus loin, la rue est complètement bloquée par des chariots que
l'on décharge pour transborder la marchandise sur un navire de
commerce. Vous poursuivez votre chemin ; la rue tourne bientôt vers
l'est pour aboutir à la rue du Col Vert. A votre gauche, vous remarquez
une autre entrée par laquelle on peut pénétrer dans le magasin de
Ragadorn. Au-delà se trouve une petite boutique avec cette enseigne
accrochée au-dessus de la porte :
MEKI MAJENOR MAÎTRE ARMURIER
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans le magasin de Ragadorn, rendez-vous au :"))
    st.page_link("tomes/tome2/page_173.py", label="173", icon="📄")
    st.write_stream(stream_text("Si vous préférez pénétrer dans la boutique de l'armurier, rendez-vous au :"))
    st.page_link("tomes/tome2/page_266.py", label="266", icon="📄")
    st.write_stream(stream_text("Si enfin vous décidez plutôt de poursuivre votre chemin en direction de l'est, rendez-vous au :"))
    st.page_link("tomes/tome2/page_310.py", label="310", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
