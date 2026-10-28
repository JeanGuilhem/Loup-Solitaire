import streamlit as st
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

check_inventory(current_page_number=46, book=3)

fr_text = """
Vous prenez la Sphère de Feu rangée dans votre tunique et vous
en séparez aussitôt les deux moitiés que vous posez derrière
vous, sur l'étroite corniche. Le Javek siffle avec force, pointant
ses deux têtes aux yeux brillants de fureur. Il éprouve de toute
évidence l'envie irrésistible de vous attaquer, mais il n'ose pas
s'approcher de la Sphère de Feu. Il essaie alors de contourner les
flammes, mais la corniche est très étroite : elle ne fait guère plus
d'une trentaine de centimètres de large. Il lui est donc impossible
de passer sans se brûler. Finalement, furieux mais impuissant,
l'étrange reptile se résigne à abandonner la partie, disparaissant
dans une cavité située au bout de la corniche. Vous pouvez à
présent récupérer votre Sphère de Feu et poursuivre votre
exploration.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_269.py", label="269", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
