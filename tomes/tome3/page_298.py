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

check_inventory(current_page_number=298, book=3)

fr_text = """
Vous découvrez un étrange Triangle de Pierre Bleue attaché à
une chaînette. La main décharnée de l'un des cadavres le tient
étroitement serré et vous êtes obligé de fracasser les phalanges
blanchies pour libérer l'objet. Si vous souhaitez conserver ce
Triangle de Pierre Bleue, passez la chaînette autour de votre cou
et glissez l'objet sous votre tunique. Inscrivez-le ensuite sur votre
Feuille d'Aventure dans la case Objets Spéciaux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_item("TRIANGLE DE PIERRE BLEUE"):
        pickup_button("TRIANGLE DE PIERRE BLEUE", key="triangle", label="Conserver le Triangle de Pierre Bleue")

    st.write_stream(stream_text("Vous pouvez quitter les lieux par un tunnel dont l'entrée se trouve dans le mur du fond ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_315.py", label="315", icon="📄")

    st.write_stream(stream_text("Vous pouvez également revenir sur vos pas et emprunter l'autre tunnel en vous rendant au :"))
    st.page_link("tomes/tome3/page_125.py", label="125", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
