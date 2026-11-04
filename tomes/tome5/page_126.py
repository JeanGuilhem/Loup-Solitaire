import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=126, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
A la faveur de l'ombre prodiguée par la tombe, vous avancez vers
la porte nord où devraient normalement se trouver une vingtaine
de soldats montant la garde. Par bonheur, il n'y en a que deux.
Soudain, le portail s'ouvre et un cavalier tend un parchemin à
l'un des Gardes avant de franchir l'entrée au galop. Le Garde jette
un coup d'œil au laissez-passer et oublie de refermer la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez soudoyer les Gardes, rendez-vous au :"))
    st.page_link("tomes/tome5/page_19.py", label="19", icon="📄")

    st.write_stream(stream_text("Si vous préférez les attaquer, rendez-vous au :"))
    st.page_link("tomes/tome5/page_119.py", label="119", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez les Disciplines Kaï du Camouflage et de la Chasse, rendez-vous au :"))
    if has_kai("Le Camouflage") and has_kai("La Chasse"):
        st.page_link("tomes/tome5/page_170.py", label="170", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_170.py", label="170", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
