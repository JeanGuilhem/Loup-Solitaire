import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=304, book=5)

fr_text = """
Le Vordak s'écroule à vos pieds mais, avant même que vous ne
puissiez vous échapper, vous êtes encerclé par les Drakkars. Un
silence de mort s'abat sur l'Arboretum. Vous vous apprêtez à
fuir en vous élançant à travers vos adversaires, mais d'autres
guerriers font leur apparition et un frisson vous parcourt l'échine :
les Drakkars qui viennent d'arriver en renfort sont tous armés
d'une arbalète. Tandis que vous poussez votre cri de guerre 
« Pour le Sommerlund ! », une volée de flèches empoisonnées vous
transperce le corps de part en part et vous vous effondrez sur le
sol. Alors que votre sang s'écoule à flots dans la terre molle de la
serre, le dernier son qui parvient à vos oreilles est le rire odieux
et moqueur du Seigneur de Ténèbres Haakon qui s'élève au-
dessus des hurlements macabres des Drakkars. Votre vie
s'achève ici et les espoirs du Sommerlund aussi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
