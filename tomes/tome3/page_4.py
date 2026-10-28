import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=4, book=3)

fr_text = """
Vous cachez le cadavre sous l'escalier et vous vous hâtez de le
fouiller. Vous y découvrez une Épée d'Os et un Disque de Pierre
Bleue. Si vous souhaitez conserver l'un ou l'autre de ces objets
(ou les deux), inscrivez-les sur votre Feuille d'Aventure dans la
case Objets Spéciaux. Vous abandonnez ensuite le cadavre et
vous montez l'escalier quatre à quatre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE D'OS", key="epee_os", label="Prendre l'Épée d'Os")
    pickup_button("DISQUE DE PIERRE BLEUE", key="disque", label="Prendre le Disque de Pierre Bleue")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
