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

check_inventory(current_page_number=205, book=3)

fr_text = """
La nuit durant, un violent blizzard fait rage, enterrant votre abri
de fortune sous une couche de neige de 3,50 mètres d'épaisseur.
Le froid vous engourdit les mains et les pieds et, peu à peu, votre
corps se vide de toute son énergie. Vous glissez alors dans un
sommeil dont vous ne vous éveillerez jamais: vous étouffez en
effet sous les neiges de Kalte. Votre mission s'achève donc ici en
même temps que votre vie.
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
