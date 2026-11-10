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

check_inventory(current_page_number=21, book=7)

fr_text = """
Au moment où le serpent géant s'affale sur le sol, un hurlement
de rage retentit derrière la grille. Soudain, des flèches de feu se
mettent à pleuvoir autour de vous, faisant éclater la pierre du
dallage et transformant instantanément en cendres fumantes
tout ce qu'elles atteignent. Sans perdre une seconde, vous
enjambez le serpent et vous partez en courant dans le tunnel
pour échapper à cette pluie mortelle. Malheureusement, vous
découvrez à votre grand désespoir que le tunnel aboutit bientôt à
une grotte étroite et basse servant d'abri à une couvée d'œufs qui
atteignent chacun la taille d'un baril de bière. Les œufs sont
posés sur un amas de vêtements en loques - probablement les
restes des précédents aventuriers pris au piège de Kazan-Oud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez examiner de plus près cette couvée, rendez-vous au :'))
    st.page_link("tomes/tome7/page_148.py", label="148", icon="📄")

    st.write_stream(stream_text('Si vous jugez préférable de chercher une issue pour sortir de ce tunnel, rendez-vous au :'))
    st.page_link("tomes/tome7/page_346.py", label="346", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
