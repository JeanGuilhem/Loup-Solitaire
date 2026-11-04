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

check_inventory(current_page_number=97, book=5)

fr_text = """
Il n'y a aucun ornement sur le coffre, excepté une petite plaque
de cuivre carrée, vissée sur le couvercle. Il n'y a pas de serrure,
mais l'instinct vous prévient de ne pas soulever le couvercle à
mains nues, au cas où le coffre serait piégé. Dans un coin de la
pièce, vous découvrez un baquet en bois et une louche. Vous
entrouvrez doucement le coffre à l'aide de la louche, puis vous
faites basculer le couvercle. La caisse n'était pas piégée, mais
vous avez cependant bien fait de vous méfier: sur un
amoncellement de masses d'armes incrustées de pierreries est
lové un Yas. Il s'agit d'un serpent vassagonien non venimeux,
mais de très grande taille. Sa tête est jaune et sa longue langue
fourchue se met à fouetter l'air tandis qu'il s'apprête à défendre
son précieux nid.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez attaquer le Yas, rendez-vous au :"))
    st.page_link("tomes/tome5/page_194.py", label="194", icon="📄")

    st.write_stream(stream_text("Si vous préférez rabattre le couvercle du coffre et sortir de l'Armurerie par la porte nord, rendez-vous au :"))
    st.page_link("tomes/tome5/page_14.py", label="14", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
