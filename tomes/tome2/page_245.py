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

check_inventory(current_page_number=245, book=2)

fr_text = """
Vous prenez la direction de l'est en longeant la rue du Col Vert et vous
remarquez bientôt, à votre gauche, une enseigne accrochée au-dessus
de la porte d'une petite boutique ; elle porte ces mots :
MEKI MAJENOR MAÎTRE ARMURIER
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez entrer dans cette boutique, rendez-vous au :'))
    st.page_link("tomes/tome2/page_266.py", label="266", icon="📄")

    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin vers l'est, rendez-vous au :"))
    st.page_link("tomes/tome2/page_310.py", label="310", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
