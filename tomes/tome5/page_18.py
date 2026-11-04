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

check_inventory(current_page_number=18, book=5)

fr_text = """
Ce n'est que lorsque le soleil a disparu derrière les sommets des
Monts du Dahir que l'on vient ouvrir la porte de votre cellule.
Vous vous préparez à rencontrer le Zakhan afin de lui demander
votre libération immédiate et l'assurance que vous pourrez
retourner, sain et sauf, au Sommerlund. Mais le Zakhan n'est pas
seul à vous attendre dans la Grande Salle. Il est accompagné d'un
invité qui a fait un long voyage pour assister à cette rencontre. Il
s'appelle Haakon, et c'est l'un des Seigneurs des Ténèbres de
Helgedad. Désarmé et impuissant, vous êtes contraint de vous
agenouiller devant Haakon. Celui-ci vous étrangle de ses propres
mains avec une délectation cruelle. Ici se termine votre vie et
tout espoir de paix pour votre pays.
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
