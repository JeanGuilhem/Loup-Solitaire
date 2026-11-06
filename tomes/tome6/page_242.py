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

check_inventory(current_page_number=242, book=6)

fr_text = """
Vos coups à la porte résonnent dans le temple, et un silence de
mort se fait dans la congrégation. Une clé grince dans la serrure
puis la porte s'ouvre lentement. Des centaines d'yeux
soupçonneux vous dévisagent tandis que vous pénétrez dans le
sanctuaire. Un prêtre vêtu d'une robe de drap d'or s'avance à
grands pas dans votre direction par la large allée centrale. Il est
rouge de colère et vous demande la raison de votre intrusion.
Lorsque vous répondez que vous êtes à la recherche de la Pierre
de la Sagesse, une bruyante clameur, mêlée de cris horrifiés,
s'élève de la foule. La porte claque sèchement derrière vous.
Comme un seul homme, la congrégation se lève et les hommes
tirent de leurs robes de bure marron de longs poignards à la lame
recourbée. Leurs yeux jettent des éclairs meurtriers tandis qu'ils
s'avancent pour vous mettre en pièces. Votre vie et votre quête
s'achèvent ici.
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
