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

check_inventory(current_page_number=80, book=6)

fr_text = """
A la lumière vacillante de la flamme, vous découvrez un grand
puits circulaire dans le sol. Tout au fond, vous distinguez une
multitude de squelettes humains, dont les os semblent ramollis
et jaunâtres, comme s'ils avaient été rongés par un acide
terriblement corrosif. Soudain, un bruit à peine perceptible
vous fait tressaillir et, en jetant un regard par-dessus votre
épaule, vous apercevez une forme qui vous glace d'effroi : un
énorme monstre bouche le tunnel ! C'est un Dakomyd, une créature
de plus de trois mètres de haut, dont les membres torses sont
prolongés chacun de huit griffes terriblement longues et
acérées, prêtes à vous tailler en pièces. Ses gros yeux
globuleux apparaissent entre des paupières jaunes et
boursouflées, et sa longue queue reptilienne fouette rageusement
l'air derrière lui. Brusquement, le monstre passe à l'attaque
avant même que vous puissiez réagir, et vous basculez dans le
puits ! Un son particulièrement odieux vous perce les tympans
quand l'ignoble créature, abaissant à l'aide d'une de ses
énormes pattes un levier encastré dans la paroi, déclenche sur
vous une pluie acide et jaune qui se met à tomber à flots du
plafond. Le redoutable liquide transperce vos vêtements en
dégageant une fumée âcre, puis s'attaque à votre chair. La
dernière chose que vous entendez est le ricanement démoniaque du
Dakomyd. Votre aventure et votre vie se terminent ici, dans les
profondeurs putrides des égouts de Tekaro.
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
