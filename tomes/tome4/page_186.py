import streamlit as st
from combat import combat
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

check_inventory(current_page_number=186, book=4)

fr_text = """
Les brigands vassagoniens surgissent soudain des ruines et se
lancent à l'attaque. Vous donnez aussitôt l'ordre de tirer. Une
pluie de flèches s'abat alors sur les hommes en armure et les
pointes d'acier transpercent leurs plastrons écarlates. La
première vague d'attaquants s'effondre. La seconde hésite. Une
autre volée de flèches oblige l'ennemi à battre en retraite parmi
les ruines. Quelques groupes de brigands ont survécu à la grêle
mortelle et sont parvenus à atteindre la barricade. D'autres sont
tués au moment où ils tentent de franchir la ligne de défense. Les
plus hardis d'entre eux réussissent cependant à passer la
barricade à proximité de l'endroit où vous vous trouvez. Soudain,
un Guerrier à la carrure impressionnante, aux longs cheveux
noirs et huileux noués derrière sa tête couturée de cicatrices,
bondit sur le chariot et vous attaque. Il vous faut le combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER VASSAGONIEN", 18, 25)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text('Vous pouvez prendre la fuite à tout moment en sautant du chariot. Rendez-vous pour cela au :'))
        st.page_link("tomes/tome4/page_66.py", label="66", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_243.py", label="243", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
