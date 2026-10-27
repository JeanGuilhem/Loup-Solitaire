import streamlit as st
from inventory import (
    check_inventory,
    choose_gifts,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=91, book=2)

fr_text = """
Le garçon est expulsé du magasin par deux gardes vêtus d'un uniforme
noir. Le marchand vous remercie et vous offre 2 objets que vous devrez
choisir dans la liste suivante : Bâton, Couverture, 2 Repas, Sac à Dos,
Poignard, 100 mètres de Corde.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    choose_gifts(
        {
            "Bâton": ("BÂTON", 1),
            "Couverture": ("COUVERTURE", 1),
            "2 Repas": ("REPAS", 2),
            "Sac à Dos": ("SAC À DOS", 1),
            "Poignard": ("POIGNARD", 1),
            "100 mètres de Corde": ("CORDE", 1),
        },
        2,
        key="gifts",
        label="Choisissez 2 objets",
    )

    st.write_stream(
        stream_text(
            "Vous remerciez ensuite le marchand et vous sortez par une porte latérale. Rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_245.py", label="245", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
