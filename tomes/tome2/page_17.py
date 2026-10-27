import streamlit as st
from combat import combat
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=17, book=2)

fr_text = """
Vous avez réussi à vous hisser à mi-corps lorsque la porte de la cale,
au-dessous de vous, s'ouvre à la volée. Un MONSTRE D'ENFER se
précipite alors et vous blesse aux jambes d'un coup de son épée noire
avant même que vous ayez pu tenter de vous enfuir. La blessure est
sérieuse et vous perdez 5 points d'ENDURANCE. Vous tombez ensuite
au fond de la cale, et il vous faut combattre la créature jusqu'à ce que
mort s'ensuive.
Il s'agit là d'un mort vivant et la puissance du Glaive de Sommer vous
permet de multiplier par deux tous les points d'ENDURANCE que
perdra la créature. Elle reste cependant insensible à la Puissance
Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-5)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-5)
    outcome = combat([("MONSTRE D'ENFER", 22, 30)], psychic_immune=True, undead=True)
    if outcome == "win":
        st.write_stream(stream_text("Vous avez tué le Monstre d'Enfer : vous pouvez quitter la cale par la porte ouverte. Rendez-vous alors au :"))
        st.page_link("tomes/tome2/page_166.py", label="166", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
