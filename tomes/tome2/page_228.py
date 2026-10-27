import streamlit as st
from inventory import (
    add_to_inventory,
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

check_inventory(current_page_number=228, book=2)

fr_text = """
Ce sont des Larnumiers, des arbres dont les fruits juteux et sucrés sont
très nourrissants. Après avoir avalé quelques-uns de ces fruits, vous
vous sentez tout revigoré et vous en cueillez l'équivalent de 2 Repas
que vous rangez dans votre Sac à Dos pour les manger plus tard. Au-delà
des arbres, une large route longe la côte en s'étendant des deux
côtés de l'horizon, à droite et à gauche. Il n'y a pas de poteau indicateur
et vous devez choisir quelle direction prendre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("REPAS", quantity=2)

    st.write_stream(stream_text('Si vous souhaitez aller à gauche, rendez-vous au :'))
    st.page_link("tomes/tome2/page_27.py", label="27", icon="📄")

    st.write_stream(stream_text('Si vous préférez aller à droite, rendez-vous au :'))
    st.page_link("tomes/tome2/page_114.py", label="114", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
