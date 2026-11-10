import streamlit as st
from inventory import (
    can_shoot,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    magnakai_rank,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=164, book=7)

fr_text = """
Vous reprenez subitement connaissance et vous portez
instinctivement la main à votre arme, au cas où... Puis, la tête
encore bourdonnante, vous vous redressez lentement et vous
inspectez les alentours. Vous vous trouvez au sommet d'un
monticule de végétation en décomposition, dressé dans le coin
d'une pièce obscure. Un relent de puanteur douceâtre emplit vos
narines : c'est l'odeur caractéristique des reptiles. Alors que vos
yeux s'habituent à la pénombre, vous remarquez parmi les
déchets qui jonchent le sol quelques fragments d'os humains. Un
faisceau de lumière blafarde, qui tombe d'une grille encastrée
dans le plafond, vient éclairer une cage thoracique, deux crânes
et plusieurs vertèbres. Soudain, la lumière vacille et, l'espace
d'une seconde, il vous semble apercevoir une espèce de tête de
mort à travers les barreaux. Immédiatement après, un rire glacial
perce le silence, et vous sentez la peur vous gagner. Pourtant, ce
n'est pas ce rire cruel et inhumain qui vous glace le sang, mais
l'apparition soudaine d'une monstrueuse tête triangulaire
émergeant du monticule même où vous vous trouvez : la tête
d'un serpent géant ! Vous vous relevez d'un bond et vous courez
dans le coin le plus éloigné de la pièce, le cœur battant à tout
rompre. Le serpent se dresse presque jusqu'au plafond ; sa mince
langue fourchue fouette rageusement l'air, et il vous fixe de son
unique œil jaune, enfoncé au milieu des écailles vertes de sa tête.
Le rire sardonique retentit à nouveau, au moment où l'ignoble
reptile commence à sortir de son nid pour glisser sournoisement
vers vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # rang de Maître Primat : 4 Disciplines Magnakaï
    animal_control = has_magnakai("Contrôle Animal") and magnakai_rank() >= 4
    bow = can_shoot()

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï du Contrôle Animal, et si vous avez atteint le rang Kaï de Maître Primat, rendez-vous au :"))
    if animal_control:
        st.page_link("tomes/tome7/page_137.py", label="137", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_137.py", label="137", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous possédez un arc, et que vous voulez l'utiliser, rendez-vous au :"))
    st.page_link("tomes/tome7/page_7.py", label="7", icon="📄", disabled=not bow)

    st.write_stream(stream_text("Si vous n'avez pas d'arc, et si vous ne maîtrisez pas la Discipline du Contrôle Animal, rendez-vous au :"))
    st.page_link("tomes/tome7/page_301.py", label="301", icon="📄", disabled=bow or animal_control)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
