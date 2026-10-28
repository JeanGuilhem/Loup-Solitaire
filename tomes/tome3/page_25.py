import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=25, book=3)

fr_text = """
Vous remarquez que l'une des créatures porte au cou un Triangle
de Pierre Bleue attaché à une chaîne. Vous pouvez le prendre si
vous le souhaitez et le passer à votre propre cou. Vous l'inscrirez
alors sur votre Feuille d'Aventure dans la case Objets Spéciaux.
Vous essuyez ensuite votre arme et vous vous hâtez de
poursuivre votre chemin, de peur qu'un autre Languabarb ne se
montre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_item("TRIANGLE DE PIERRE BLEUE"):
        pickup_button("TRIANGLE DE PIERRE BLEUE", key="triangle", label="Prendre le Triangle de Pierre Bleue")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_284.py", label="284", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
