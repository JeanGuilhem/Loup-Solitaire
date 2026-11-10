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

check_inventory(current_page_number=74, book=7)

fr_text = """
Ces tapisseries ressemblent à celles que vous avez déjà vues dans
la partie inférieure de Kazan-Oud ; elles sont d'une extrême
beauté et probablement d'une grande valeur. Cependant en les
soulevant, vous découvrez une porte secrète. Grâce à vos
connaissances de base Kaï, vous décelez un minuscule bouton
dans le mur. Vous appuyez dessus et, aussitôt, la porte coulisse
lentement, révélant un tunnel circulaire en acier poli. Vous y
pénétrez rapidement et la porte se referme sur vous. Il était
temps car, à ce moment précis, vous entendez les gardes de
Zahda faire irruption dans le vestibule ! Après avoir parcouru le
tunnel d'acier sur une vingtaine de mètres, vous arrivez à la
hauteur d'une porte circulaire, encastrée dans la paroi de gauche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez ouvrir cette porte et entrer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_15.py", label="15", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer à suivre le tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_90.py", label="90", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
