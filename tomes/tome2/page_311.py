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

check_inventory(current_page_number=311, book=2)

fr_text = """
Vous tombez à plat ventre dans un enchevêtrement d'épaisses fougères
tandis que résonnent à vos oreilles le cliquetis des épées et les cris
terrifiants des Monstres d'Enfer. Vous êtes à moitié assommé et vous ne
pouvez plus faire un geste. Enfin, une main vous saisit le bras et vous
remet debout d'un geste vigoureux. C'est le Lieutenant Général Rhygar,
le visage ensanglanté, son armure bosselée et noircie. Il faut fuir ces
démons ! s'exclame-t-il, la force de nos épées ne peut rien contre eux. »
Vous apercevez alors les silhouettes de six Monstres d'Enfer occupés à
anéantir par leur seule Puissance Psychique les malheureux soldats du
Lieutenant Général. Or, tandis qu'ils se concentrent ainsi, vous
parvenez à vous échapper, Rhygar et vous, en vous glissant dans les
broussailles pour atteindre l'abri de la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_299.py", label="299", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
