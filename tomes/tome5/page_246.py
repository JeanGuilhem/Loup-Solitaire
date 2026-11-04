import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=246, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous ouvrez la porte avec la Clé de Cuivre et vous vous précipitez
dans le jardin. A peine avez-vous refermé la porte que vous
entendez le bruit des flèches qui viennent rebondir sur les barres
de fer. Des buissons et des arbres exotiques aux parfums délicats
bordent un joli bassin rempli d'eau bleue. C'est un spectacle
ravissant, mais vous n'osez pas vous arrêter pour en jouir
tranquillement. En effet, les Drakkars et les Gardes du Palais
savent que vous êtes dans ce jardin et vous devez impérativement
reprendre votre course si vous voulez avoir une chance de leur
échapper. Derrière une colonnade, une volée de marches grimpe
jusqu'à un petit portail encastré dans le mur du Palais supérieur.
A votre droite, une allée s'enfonce dans l'épais feuillage des
arbres et des arbustes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez gravir les marches qui mènent au petit portail, rendez-vous au :"))
    st.page_link("tomes/tome5/page_352.py", label="352", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre le sentier sinueux, rendez-vous au :"))
    st.page_link("tomes/tome5/page_391.py", label="391", icon="📄")

    st.write_stream(stream_text("Si vous possédez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome5/page_220.py", label="220", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_220.py", label="220", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
