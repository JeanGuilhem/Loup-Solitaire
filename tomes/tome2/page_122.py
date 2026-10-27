import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=122, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Cette rue longe les murs de la ville en direction du nord. Sur votre
droite, vous remarquez une boutique dont la porte est de couleur
orange. A la différence des autres boutiques de la rue, celle-ci ne porte
aucune enseigne. C'est alors que vous revient en mémoire le récit qu'un
Seigneur Kaï vous avait fait il y a environ un an à son retour d'un
voyage dans la ville de Ragadorn. Il vous avait parlé de cette porte
orange à plusieurs reprises.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_96.py", label="96", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_96.py", label="96", icon="📄", disabled=True)
    st.write_stream(stream_text("Sinon, utilisez la Table de Hasard pour obtenir un chiffre."))
    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome2/page_46.py", label="46", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome2/page_112.py", label="112", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
