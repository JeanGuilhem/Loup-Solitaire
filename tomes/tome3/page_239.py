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

check_inventory(current_page_number=239, book=3)

fr_text = """
Vous perdez très vite conscience. Vous venez en effet de
succomber au pouvoir terrifiant d'une ancienne Pierre Maudite,
un pouvoir auquel nul être vivant ne peut survivre. La mort est
inévitable et ne tardera plus. Peut-être éprouverez-vous malgré
tout quelque consolation à apprendre que votre cadavre sera
bientôt découvert par un Barbare des Glaces qui l'amènera
devant Vonotar (en même temps que la Pierre Maudite). Le
traître éprouvera alors tant de joie à vous voir mort qu'il
ordonnera que votre corps soit conservé dans un bloc de glace et
exposé dans sa salle du Trône, comme un trophée. Mais les
radiations de la Pierre Maudite, restée dans votre poche,
atteindront le sorcier maléfique en dépit de la couche de glace et
Vonotar devra subir de longues souffrances avant de mourir à
son tour. Bien entendu, votre mission s'achève ici en même
temps que votre vie.
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
