import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=232, book=7)

fr_text = """
Votre flèche transperce le bras du chef des créatures, et un épais
liquide vert s'échappe de sa blessure. Il vacille en poussant un
affreux hurlement, et vous assistez alors, surpris et dégoûté, à
une horrible scène : ses compagnons se jettent sur lui, arrachent
le membre blessé avec leurs dents et leurs griffes, puis le
dévorent avidement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez tirer une autre flèche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_152.py", label="152", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous préférez passer votre arc autour de l'épaule et fuir au plus vite ces créatures vampiriques en courant vers l'entrée de l'autre tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_241.py", label="241", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
