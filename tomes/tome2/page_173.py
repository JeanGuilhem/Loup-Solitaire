import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=173, book=2)

fr_text = """
Vous pénétrez dans un somptueux magasin où sont exposées les
marchandises les plus raffinées qu'on puisse trouver au nord de
Magnamund. Même à cette heure tardive, l'endroit est animé : des
capitaines et de riches commerçants marchandent en effet l'achat ou
l'échange de leurs denrées. Le propriétaire du magasin est un jeune
guerrier qui préside aux enchères du haut d'un fauteuil de bois sculpté
suspendu par quatre chaînes. Ces hommes sont tous vêtus d'armures
noires et leurs boucliers portent pour emblème l'image d'un vaisseau
noir surmonté d'une crête rouge. Vous surprenez alors un jeune garçon
en train de voler la bourse accrochée à la ceinture d'un marchand. Son
forfait accompli, le garnement glisse son butin dans sa botte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous décidez d'attraper le garçon pour lui faire rendre la bourse, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_91.py", label="91", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez suivre le jeune homme au-dehors et lui dérober la bourse à votre tour, "
            "rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_6.py", label="6", icon="📄")

    st.write_stream(
        stream_text(
            "Enfin, si vous choisissez de faire comme si vous n'aviez rien vu pour consacrer plutôt "
            "votre attention aux marchandises exposées, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_283.py", label="283", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
