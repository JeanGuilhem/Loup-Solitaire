import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=302, book=4)

fr_text = """
Le coffre n'est pas fermé à clé. Ce qui vient d'arriver à vos
hommes vous rend cependant très prudent, et vous décidez de ne
pas prendre de risques. Vous tenant à l'écart du coffre, vous
soulevez le couvercle de la pointe de votre arme et vous le
rabattez d'un coup sec. Vous attendez un instant en retenant
votre souffle, mais rien ne se produit. Le propriétaire du coffre
estime sans doute que le piège aménagé dans le passage suffit à
le protéger des voleurs. Le coffre contient nombre d'objets de
valeur : des assiettes et des coupes d'or incrustées de pierreries,
des colliers de turquoise, des perles, des statuettes de jade et une
pierre précieuse d'un grand prix. Vous contemplez ces richesses
avec émerveillement, mais vous décidez de n'en emporter
aucune. Elles seraient trop lourdes, en effet, et inutiles à votre
mission. Vous remarquez alors, sous les assiettes d'or, un sac de
cuir. Vous le retirez du coffre et vous reconnaissez aussitôt sa
forme caractéristique ; il s'agit d'un sac d'herboriste qui contient
les objets suivants :
— 2 flacons de Potion de Laumspur : chaque dose vous permet de
regagner 4 points d'ENDURANCE ;
— 1 fiole de Potion d'Aléther : elle vous permet d'augmenter de 2
points votre HABILETÉ au cours d'un combat (et un seul) ;
— 1 flacon d'Eau Bénite.
Si vous souhaitez conserver l'un ou l'autre de ces objets,
inscrivez-les sur votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("POTION DE LAUMSPUR", key="laumspur_1", label="Prendre un flacon de Potion de Laumspur")
    pickup_button("POTION DE LAUMSPUR", key="laumspur_2", label="Prendre un flacon de Potion de Laumspur")
    pickup_button("FIOLE D'ALÉTHER", key="alether", label="Prendre la fiole de Potion d'Aléther")
    pickup_button("EAU BÉNITE", key="eau_benite", label="Prendre le flacon d'Eau Bénite")

    st.write_stream(stream_text("Dirigez-vous à présent vers la porte située de l'autre côté en vous rendant au :"))
    st.page_link("tomes/tome4/page_131.py", label="131", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
