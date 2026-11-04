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

check_inventory(current_page_number=202, book=5)

fr_text = """
Vous passez sous un porche voûté flanqué de deux tours
coniques dont les toits en cuivre brillent comme de l'or. Puis vous
arrivez sur une grande place noire de monde où se tient un
marché. De nombreux commerçants haranguent la foule et les
marchandages vont bon train. On peut acheter ici toutes sortes
d'objets colorés, des tapis exotiques et une grande variété de
produits agricoles. La partie nord du marché est consacrée à la
vente aux enchères de Douggas, des animaux du désert au poil
lisse, et très bruyants. Ceux-ci ont été parqués dans un enclos
attenant aux écuries près duquel se pressent les futurs acheteurs.
Juste derrière les écuries, une rue disparaît dans le quartier des
fabricants de tapis d'Ikaresh.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans les écuries, rendez-vous au :"))
    st.page_link("tomes/tome5/page_309.py", label="309", icon="📄")

    st.write_stream(stream_text("Si vous voulez demander à l'un des marchands où se trouve Tipasa, rendez-vous au :"))
    st.page_link("tomes/tome5/page_248.py", label="248", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter le marché, traversez la place et rendez-vous au :"))
    st.page_link("tomes/tome5/page_386.py", label="386", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
