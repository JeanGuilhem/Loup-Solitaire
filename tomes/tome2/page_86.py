import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    receive_gold,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=86, book=2)

fr_text = """
De ce côté du port, de nombreux navires sont amarrés ; il y a là des
bateaux de toutes sortes qui battent pavillon de tous pays. Le fleuve
Dom qui traverse la ville de Ragadorn connaît toujours une très grande
activité : c'est la voie navigable la plus importante de la région. Vous
êtes sur le point d'abandonner vos recherches lorsque vous repérez
enfin le bateau de pêche de vos malandrins. Il n'y a personne à bord,
mais une fouille en règle vous permet de découvrir une Masse d'Armes
et trois Pièces d'Or dissimulées dans un hamac soigneusement plié. Une
étiquette est cousue sur le hamac et porte ces mots : Taverne de l'Étoile
du Nord rue de la Bernicle. Vous prenez la Masse d'Armes et les Pièces
d'Or et vous retournez sur la place du Poteau de Pierre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    receive_gold(3)
    pickup_button("MASSE D'ARMES", key="masse", label="Prendre la Masse d'Armes")

    st.write_stream(
        stream_text(
            "Si vous souhaitez aller vers l'est, le long de la rue de la Bernicle, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_215.py", label="215", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez aller au sud, en suivant le Dock de la rive Ouest, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_303.py", label="303", icon="📄")

    st.write_stream(
        stream_text(
            "Enfin, si vous choisissez plutôt de prendre la direction du nord en empruntant la rue du "
            "Butin, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_129.py", label="129", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
