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

check_inventory(current_page_number=88, book=5)

fr_text = """
L'affiche est couverte de caractères vassagoniens écrits de droite
à gauche. Vous avez fort bien fait d'apprendre cette langue
lorsque vous étiez à bord de la galère, car vous êtes à présent
capable de traduire aisément la proclamation suivante :
Son illustre Majesté, le Zakhan Moudalla le très-haut, repose
désormais en paix au royaume du Majhan. Puisse son esprit
vivre à tout jamais ! Par la grâce du Conseil de Kadi, de
l'Assemblée de Kara-Kala et de la Cour de Justice de
Barrakeesh, il a été décrété que Kimah, Émir de Ferufezan et
Protecteur de la Mer de la Sécheresse, montera sur le trône de
Vassagonie en tant que successeur légal de Moudalla. Grâce à
l'unité des Sept Cités, le Zakhan Kimah mènera son peuple sur
les sentiers de la gloire. Long soit son règne !
Une bagarre éclate soudain au bout de la ruelle tandis qu'une
patrouille de Sharnazims tente de se frayer un chemin dans la
foule. Dans la confusion, un étalage de fruits est renversé et son
propriétaire se met à maudire d'une voix forte la maladresse des
soldats. Subitement, un silence de mort s'abat sur les lieux :
l'infortuné marchand vient d'être décapité pour son insolence.
Tournant les talons, vous rebroussez rapidement chemin en
pataugeant dans le caniveau peu profond qui longe la venelle
malodorante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_113.py", label="113", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
