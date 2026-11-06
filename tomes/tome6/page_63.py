import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=63, book=6)

fr_text = """
Le sentier qui mène au Château de Taunor est abrupt et glissant
et il serait bien trop risqué de l'emprunter à cheval. Cyrilus
vous propose de rester en bas et de garder votre monture tandis
que vous irez recueillir un peu d'eau de source, puisque son
grand âge, vous dit-il, l'empêche de grimper une pente aussi
escarpée. Cependant, vous vous doutez qu'il s'agit là d'un
prétexte pour faire un petit somme en votre absence. Le château
ne se trouve qu'à un kilomètre à peine de la grand-route, mais
il vous faut pourtant plus d'une demi-heure pour atteindre le
piton rocheux où il se dresse. Les murs croulants sont
recouverts d'une végétation humide et touffue, et
l'impressionnant à-pic qui surplombe les ruines projette sur le
donjon une ombre sinistre et menaçante. Vous avancez en vous
repérant au murmure de l'eau, jusqu'à ce que vous arriviez à une
petite chapelle. Là, vous découvrez un mince filet d'eau limpide
et scintillante, coulant goutte à goutte par une fissure de la
pierre de l'autel. Alors que vous vous agenouillez pour remplir
votre flacon de verre, vous percevez soudain un léger bruit :
vous n'êtes pas seul ici !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, rendez-vous au :"))
    if has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_162.py", label="162", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_162.py", label="162", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    if has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_278.py", label="278", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_278.py", label="278", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
