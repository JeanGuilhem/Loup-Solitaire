import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=232, book=3)

fr_text = """
Après avoir réussi à franchir la crevasse, vous poursuivez votre
chemin pendant presque une heure avant d'arriver enfin devant
le glacier de Viad. Son ascension est une entreprise redoutable :
il présente en effet un mur de glace lisse en à-pic qui s'élève à
plus de 30 mètres de hauteur. Il vous faut décharger les
traîneaux puis hisser le matériel au sommet avant de le recharger
à nouveau. Les chiens Kanu passent leur temps à se battre entre
eux tandis que vous menez à bien cette tâche fastidieuse et
épuisante. Lorsque tout le matériel se trouve enfin sur le glacier,
vous vous apercevez que vos provisions, singulièrement
malmenées par ce transport, ne sont plus qu'une bouillie peu
appétissante ; il faut cependant vous en contenter en guise de
dîner. Vous dressez la tente au sommet du mur de glace, au creux
d'une cuvette naturelle et vous vous installez pour profiter d'une
nuit de repos bien méritée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez un chiffre de 0 à 6, rendez- "
            "vous au 85. Si vous tirez 7, 8 ou 9, rendez-vous au 300."
        )
    )
    roll = hazard_roll()
    if roll is not None and roll <= 6:
        st.page_link("tomes/tome3/page_85.py", label="85", icon="📄")
    elif roll is not None:
        st.page_link("tomes/tome3/page_300.py", label="300", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
