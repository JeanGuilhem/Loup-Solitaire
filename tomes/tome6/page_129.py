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

check_inventory(current_page_number=129, book=6)

fr_text = """
Soudain, c'est le branle-bas de combat : des cloches d'alarme se
mettent à sonner, des voix à crier et des pas à résonner dans
toutes les rues de la ville. Une troupe de soldats vous
encercle. A la lumière vacillante de leurs torches, leurs
visages semblent se tordre et grimacer cruellement. L'extrême
fatigue que vous éprouvez anéantit toutes vos forces : on vous
tire à bas de votre selle et l'on vous désarme avant même que
vous ne songiez à réagir. Puis on vous ligote à l'aide de
grosses chaînes et l'on vous pousse sans ménagement à
l'intérieur d'un cachot sombre et humide. Une vague de terreur
vous submerge lorsque vous entr'apercevez, clouée sur la porte
de la cellule, une affiche représentant votre portrait ! On a
écrit dessous : «Condamné à mort sur l'ordre du noble Roark,
Seigneur d'Amory. » Dans l'heure qui suit, on vous traîne devant
le bourreau et, la tête sur le billot, vous entendez résonner le
rire sardonique de Roark, avant que le tranchant de la hache
s'abatte sur votre cou. Votre aventure et votre vie s'achèvent
ici.
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
