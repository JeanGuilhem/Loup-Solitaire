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

check_inventory(current_page_number=300, book=7)

fr_text = """
Vous montez les marches en vous frayant un chemin parmi la
foule et courez à toute vitesse vers le complexe carcéral. Des
vagues d'explosions successives secouent violemment les
fondations de la forteresse, et d'énormes blocs de pierre et de fer
tombent un peu partout du plafond. Vous traversez le complexe
en fauchant ce qui entrave votre progression et vous courez le
long du seul couloir qui n'a pas été obstrué par les chutes de
pierre. Vous êtes au milieu d'un escalier en colimaçon lorsque
retentit soudain un énorme grondement suivi d'un grincement
métallique. Les créatures qui se pressent autour de vous
poussent des cris de terreur, mais leurs voix se perdent dans le
fracas assourdissant de l'escalier qui s'effondre et qui tombe dans
un gouffre rempli de lave, quelque cent cinquante mètres plus
bas. Votre vie et votre aventure s'achèvent ici, dans les ruines de
Kazan-Oud.
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
