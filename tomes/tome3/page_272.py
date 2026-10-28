import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=272, book=3)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Tandis que l'immonde Akranionor meurt à vos pieds dans un
ultime tremblement, Vonotar interrompt son attaque psychique
et va se réfugier derrière le Trône du Brumalmarc. Loi-Kymar est
commotionné, mais il a survécu à l'épreuve. Il vous rejoint alors
au bord du fossé dans lequel il jette une poignée d'herbes.
Quelques secondes plus tard, un enchevêtrement de plantes
grimpantes apparaît, formant un pont qui permet de passer de
l'autre côté. Vous vous précipitez vers la plateforme, et vous êtes
arrivé à mi-chemin lorsque Vonotar se montre à nouveau,
brandissant une baguette de cristal. Il vise la passerelle végétale
et un cône de givre jaillit aussitôt de l'extrémité de sa baguette.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome3/page_213.py", label="213", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_213.py", label="213", icon="📄", disabled=True)
        st.write_stream(stream_text("Sinon, utilisez la Table de Hasard pour obtenir un chiffre. Entre 0 et 3, rendez-vous au 143. Entre 4 et 9, rendez-vous au 58."))
        roll = hazard_roll()
        if roll is not None and roll <= 3:
            st.page_link("tomes/tome3/page_143.py", label="143", icon="📄")
        elif roll is not None:
            st.page_link("tomes/tome3/page_58.py", label="58", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
