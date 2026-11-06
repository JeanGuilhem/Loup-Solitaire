import streamlit as st
from inventory import (
    check_inventory,
    clear_flag,
    display_inventory,
    end_page,
    is_new_page,
    pickup_button,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# fait posé : "Arc en Chêne" (+3 aux tirs à l'Arc sur la Table de Hasard, voir page 268)

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=252, book=6)

fr_text = """
Une immense ovation s'élève de la foule lorsque votre flèche
atteint la cible. Vous avez gagné ! Les villageois sont très
heureux d'avoir assisté à un tournoi d'un niveau si relevé et se
précipitent vers vous pour vous féliciter. Le petit homme au
pourpoint galonné vous remet le prix du vainqueur : un magnifique
Arc en Chêne. A chaque fois que l'on vous demandera d'utiliser la
Table de Hasard pour obtenir un chiffre et que vous utiliserez un
Arc, cette arme vous permettra d'ajouter 3 points au chiffre
obtenu. Inscrivez votre Arc dans la case Armes de votre Feuille
d'Aventure sous le nom « Arc en Chêne », et notez ses
caractéristiques. Vous faites un petit discours aux villageois
pour les remercier de leur aimable accueil, puis vous partez
rejoindre Cyrilus pour lui annoncer la bonne nouvelle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Fait posé : « tournoi de tir à l'arc gagné » (testé au 325) ; l'arc emprunté est rendu
    if is_new_page():
        set_flag("tournoi de tir à l'arc gagné")
        for flag in ("arc emprunté", "arc Jakan", "arc de Kalte"):
            clear_flag(flag)
    pickup_button("ARC EN CHÊNE", key="t6_252_arc", label="Prendre l'Arc en Chêne")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
