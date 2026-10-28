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

check_inventory(current_page_number=6, book=3)

fr_text = """
Vous progressez dans l'obscurité en tenant votre arme en avant,
au cas où un obstacle se dresserait sur votre chemin. Le couloir
se prolonge en direction du nord sur une certaine distance, puis
il tourne brusquement vers la droite. A quelques mètres devant
vous, vous apercevez à présent une lumière provenant d'une
autre ouverture. Au-delà de cette source de lumière, un peu plus
loin dans le tunnel, un escalier s'enfonce dans les ténèbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez jeter un coup d'œil à travers cette ouverture, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_224.py", label="224", icon="📄")

    st.write_stream(stream_text("Si vous préférez descendre l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome3/page_166.py", label="166", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
