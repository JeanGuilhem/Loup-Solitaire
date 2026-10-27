import streamlit as st
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

check_inventory(current_page_number=341, book=2)

fr_text = """
Il ne reste plus du malheureux navire qu'une coque fracassée et les
lambeaux de voiles. Vous insistez auprès du capitaine pour qu'il fasse
rechercher d'éventuels survivants, mais il ignore votre demande et
ordonne à ses hommes d'équipage de poursuivre leur tâche. Alors,
tandis que vous vous éloignez de l'épave, un sentiment d'appréhension
vous envahit peu à peu : et si un sort semblable vous attendait, vous
aussi ? La gorge sèche, vous descendez sur le pont inférieur pour
rejoindre votre cabine en prenant bien soin d'en fermer la porte à clé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
