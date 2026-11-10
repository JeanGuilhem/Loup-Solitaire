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

check_inventory(current_page_number=159, book=7)

fr_text = """
Vous pénétrez dans la salle du trône de Zahda, une immense
pièce toute dallée de marbre poli. L'écho de vos pas se répercute
sur les gradins circulaires au fur et à mesure que vous approchez
du puits central. L'endroit est désert ; seules les flammes
vacillantes qui lèchent l'estrade en fer noir apportent un peu de
lumière. « Ainsi, vous osez défier la puissance de Zahda ? » tonne
soudain une voix amplifiée par l'imposant volume de la pièce,
alors qu'un faisceau de lumière éblouissante, issu du trône, se
braque sur vous. « Vous osez vous dresser contre le Maître de
Kazan-Oud ! » Vous tentez désespérément d'échapper au rayon
aveuglant, mais vous ne pouvez faire le moindre geste ; vos
muscles sont tout engourdis et restent inertes, paralysés par le
rayon de Zahda. « Je connais vos intentions, reprend la voix
tonitruante, car votre identité me fut révélée lorsque vous étiez
dans le labyrinthe. Vous êtes le Seigneur Kaï, celui qu'on nomme
Loup Solitaire. Vous êtes venu ici pour voler ce qui m'appartient ;
pour ce genre de crime, il n'y a qu'un châtiment : la mort ! » A
peine l'écho de ces sinistres paroles s'est-il tu, qu'une boule
d'énergie foudroyante jaillit du trône en fusant vers vous comme
un soleil de feu. Vous grillez vif et, la seconde d'après, il ne reste
plus rien de votre corps. Votre aventure se termine ici.
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
