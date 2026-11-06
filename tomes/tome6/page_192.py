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

check_inventory(current_page_number=192, book=6)

fr_text = """
Vous pataugez dans la vase qui vous arrive jusqu'aux chevilles,
lorsque soudain vous apercevez devant vous des petites lueurs
rouges dans l'obscurité. Les lumières deviennent de plus en plus
brillantes et vous réalisez, horrifié, qu'il s'agit de deux autres
Yamsarks. Ils s'approchent de vous en poussant d'affreux
ricanements et des cris assourdissants. Vous avez pénétré par
mégarde dans leur territoire et vous voilà pris au piège. Vous
vous battez vaillamment mais finalement vous succombez, taillé en
pièces par ces horribles créatures. Personne dans ce passage
sombre et humide n'a entendu vos appels au secours. Votre vie
s'achève ici, dans les cachots du Château de Taunor.
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
