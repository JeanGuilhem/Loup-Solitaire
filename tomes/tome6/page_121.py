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

check_inventory(current_page_number=121, book=6)

fr_text = """
Le magasin recèle une fascinante collection de créatures
empaillées, immortalisées dans une attitude étonnante et mises
en scène de façon réaliste. Un loup à deux têtes monte la garde
à l'entrée d'une caverne ; à côté, un Baknar est allongé sur une
étendue neigeuse et, un peu plus loin, un Ganthi des sables lape
l'eau d'une source, dans une oasis reconstituée où se dressent
de grands Toas. Vous êtes en train d'examiner une tête d'Itikar
remarquablement conservée, lorsque vous entendez soudain
s'élever derrière vous une voix douce et distinguée : « Bonsoir,
gentilhomme, soyez le bienvenu en mon établissement. » Un homme
de haute taille, à l'allure aristocratique et vêtu d'un habit
richement brodé, s'avance vers vous et s'incline. Il semble
apprécier l'intérêt que vous portez à ses réalisations et vous
propose aimablement de vous faire visiter le reste de son
atelier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez le suivre, rendez-vous au :"))
    st.page_link("tomes/tome6/page_345.py", label="345", icon="📄")

    st.write_stream(stream_text("Si vous préférez décliner poliment son offre et sortir du magasin, rendez-vous au :"))
    st.page_link("tomes/tome6/page_149.py", label="149", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
