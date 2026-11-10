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

check_inventory(current_page_number=73, book=7)

fr_text = """
Vous vous approchez d'une caisse et vous en arrachez le
couvercle aussi facilement que s'il s'agissait de peler une orange
trop mûre. Le bois pourri s'effrite sous vos doigts et tombe en
poussière sur des plats d'étain ternis, empilés au fond de la
caisse. D'un coup de botte, vous défoncez une autre caisse et vous
entendez un bruit de porcelaine brisée à l'intérieur : ce sont
d'anciens vases Kakush qui, vous vous en souvenez, faisaient
partie de la cargaison d'un navire marchand ayant fait naufrage il
y a plus de dix ans. Alors que vous vous apprêtez à quitter la
pièce, quelque chose attire votre regard : il s'agit d'un tube en
métal qui dépasse de derrière un tonneau vide. Contrairement à
tout ce qui se trouve dans cet endroit humide et malsain, l'objet
est intact et flambant neuf. Après avoir ôté l'embout du cylindre,
vous en renversez le contenu au creux de votre main. Il en tombe
un petit bout de parchemin et un Diamant. (Si vous voulez
conserver cet Objet Spécial, inscrivez-le sur votre Feuille
d'Aventure et glissez-le dans votre poche.) Sur le parchemin, un
serpent est dessiné à l'encre rouge. Il n'a qu'un seul et unique œil
et il est enroulé autour du nombre 123. Inscrivez ce nombre dans
la marge de votre Feuille d'Aventure - cela pourrait vous être
utile au cours de votre expédition. Après avoir vérifié qu'il n'y a
plus rien d'intéressant dans la pièce, vous sortez et vous vous
dirigez à grands pas vers l'escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("DIAMANT", key="diamant", label="Conserver le Diamant")
    st.info("Nombre à noter dans la marge de votre Feuille d'Aventure : **123**")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_11.py", label="11", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
