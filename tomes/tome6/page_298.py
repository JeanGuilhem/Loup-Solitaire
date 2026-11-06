import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# fait posé : "arc Jakan" (-2 HABILETÉ au tournoi ; un 0 à la Table de Hasard brise l'arc : page 335)

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=298, book=6)

fr_text = """
Le Jakan est un grand arc utilisé par les pêcheurs de la côte de
Vassagonie. Il convient parfaitement pour la chasse aux barbidahns
et aux squids qui vivent dans les récifs de Barrakeesh, mais c'est
un arc de tir médiocre. De plus, l'arc que vous avez choisi
présente une fissure sur toute la longueur et il peut se casser à
tout moment. Aussi, diminuez votre total d'HABILETÉ de 2 points au
début du tournoi. Par ailleurs, si vous tirez un 0 dans la Table
de Hasard, au cours de la compétition, votre arc se brisera et
vous devrez vous rendre immédiatement au 335. (Notez bien ce
numéro dans la marge de votre Feuille d'Aventure, au cas où cette
mésaventure vous arriverait.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        set_flag("arc emprunté")
        set_flag("arc Jakan")
    st.info("Votre arc fêlé est noté : un 0 tiré pendant le tournoi vous enverra au paragraphe 335.")

    st.write_stream(stream_text("Pour commencer le tournoi, rendez-vous au :"))
    st.page_link("tomes/tome6/page_340.py", label="340", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
