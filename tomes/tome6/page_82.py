import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=82, book=6)

fr_text = """
La cale du bateau est pleine de chevaux ; non pas des bêtes de
trait utilisées par les marchands ambulants, mais de fortes et
vigoureuses montures portant sur leurs flancs musclés de
nombreuses cicatrices de bataille. Vous dessellez votre jument
et, après avoir rempli sa mangeoire, vous remontez sur le pont.
Au moment où vous émergez de la soute, une voix tonitruante crie
votre nom, et vous apercevez, en levant les yeux, le capitaine
du bateau : c'est le chef des mercenaires que vous avez
rencontré à l'Auberge des Épées Croisées ! « Bienvenue à toi,
mon ami ! s'exclame-t-il en vous donnant une grande claque dans
le dos. Ainsi, tu as changé d'avis et tu viens te joindre à ma
troupe de valeureux guerriers ! » Avant même que vous puissiez
répondre, le Capitaine et ses hommes - qui affichent tous un
penchant certain pour la boisson - se mettent en route pour
accomplir une mission de la plus haute importance : partir à la
recherche du magasin aux vins ! Vous êtes bien trop las, quant à
vous, pour leur emboîter le pas. La couchette qui vous attend
dans votre cabine et la perspective d'une bonne nuit de sommeil
sont tout ce qui vous intéresse pour l'instant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_341.py", label="341", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
