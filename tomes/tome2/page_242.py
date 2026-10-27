import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=242, book=2)

fr_text = """
Pendant la plus grande partie de votre séjour à Hammardal, vous vous
entraînez à manier le Glaive de Sommer. Jour après jour, votre habileté
s'accroît et, à mesure que vous progressez, vous en apprenez davantage
sur les vertus de cette arme fabuleuse. Chaque fois que vous utiliserez
le glaive dans un combat, votre total d'HABILETÉ sera augmenté de 8
points (de 10 points si vous avez choisi la Discipline Kaï de la Maîtrise
des Armes et que le sort vous a donné cette maîtrise à l'épée). Le glaive
a en outre la propriété d'annuler les effets de toute pratique magique
exercée contre vous par un adversaire ; il vous permettra aussi de
multiplier par 2 tous les points d'ENDURANCE perdus par des morts
vivants (les Monstres d'Enfer, par exemple) au cours des combats qu'il
vous faudra peut-être livrer contre eux. Enfin, vous avez pleinement
conscience que le Glaive de Sommer est la seule et unique arme, sur
toutes les terres de Magnamund, qui ait le pouvoir d'ôter la vie à un
Maître des Ténèbres ; il n'est donc pas étonnant que ces derniers aient
résolu de vous tuer à tout prix.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_152.py", label="152", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
