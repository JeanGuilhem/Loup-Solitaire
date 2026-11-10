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

check_inventory(current_page_number=130, book=7)

fr_text = """
Vous fixez la créature droit dans les yeux et vous lui ordonnez
impérativement de cesser son attaque. Immédiatement, l'ignoble
bête vermiforme se retourne sur le dos et se met à battre l'air de
ses courtes pattes : votre volonté l'a emporté sur cet esprit simple
et vulnérable. Alors que la misérable chose se remet péniblement
sur ses pattes, sa tête disparaît dans la brume. Il se produit
simultanément un craquement assourdissant, et un éclair de
lumière bleue vient s'enrouler comme un serpent autour de son
cou. Une répugnante odeur de chair grillée envahit l'atmosphère
tandis que la créature se contorsionne dans les affres de l'agonie.
Une fois cette danse macabre terminée, le banc de brume
s'évanouit ; au-dessus de vous, dans la pénombre, vous
distinguez une passerelle munie d'une plate-forme d'observation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez prendre appui sur le cadavre du vermiforme pour vous hisser sur cette plate-forme, rendez-vous au :"))
    st.page_link("tomes/tome7/page_294.py", label="294", icon="📄")

    st.write_stream(stream_text("Si vous préférez enjamber l'ignoble créature, puis continuer à avancer dans le tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_46.py", label="46", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
