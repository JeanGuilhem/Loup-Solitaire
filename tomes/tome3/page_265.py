import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=265, book=3)

fr_text = """
Cette étrange créature est un Serpent de Cristal, un nécrophage
se nourrissant des restes d'animaux qui ont eu l'imprudence
d'entrer dans sa caverne. Sa peau très dure est presque
transparente et l'on voit ses organes palpiter à l'intérieur de son
corps. Le monstre ouvre sa gueule de cristal, laissant apparaître
deux rangées de dents acérées. Le dos plaqué contre la porte de
pierre, vous n'avez aucune possibilité de fuite et il vous faut
combattre la créature jusqu'à la mort. Le Serpent de Cristal est
invulnérable à la Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("SERPENT DE CRISTAL", 15, 30)], psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome3/page_3.py", label="3", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
