import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=350, book=6)

fr_text = """
La peau de sa tête se plisse et se craquèle comme si une vague se
gonflait et déferlait sous l'épaisse carapace de son crâne. Les os
translucides de sa tête s'effritent et tombent sur le sol. Le corps
difforme s'affaisse et se recroqueville et, en l'espace de quelques
secondes, il ne reste plus du Dakomyd qu'un minuscule tas de
poussière sur le sol de la crypte. Le temps a enfin terrassé cette
ancienne terreur ! La puissante lumière dorée émise par la Pierre
de la Sagesse de Varetta commence à s'affaiblir, et vous regardez
l'objet de votre quête : ce n'est plus maintenant qu'une simple
boule de verre, creuse et transparente, tout à fait ordinaire. Mais
vous avez rempli votre mission, et ses pouvoirs se sont transmis à
votre corps et à votre esprit. Sa force et sa sagesse font désormais
partie intégrante de vous-même, et cette transmission marque le
début d'un nouveau défi dans votre quête du Magnakaï. Mais
attention ! cette quête vous conduira au cœur d'un dangereux
royaume où régnent des forces maléfiques qui ont acquis un
immense pouvoir depuis qu'Aigle du Soleil a le premier accompli
la quête de la Sagesse Magnakaï. Si vous avez le courage et la
sagesse d'un vrai Maître Kaï, une nouvelle aventure vous attend
dans le septième volume de la série Loup Solitaire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.balloons()
    st.success(
        "**Mission accomplie !** Le Dakomyd n'est plus que poussière et les pouvoirs de la Pierre de la Sagesse "
        "de Varetta se sont transmis à votre corps et à votre esprit : votre quête du Magnakaï peut se poursuivre."
    )
    st.info("Le tome 7 n'est pas encore disponible dans l'application : votre héros est sauvegardé en attendant.")
    st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
