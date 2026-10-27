import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=191, book=2)

fr_text = """
Un peu plus loin, la rue pavée tourne brusquement vers la droite. Vous
vous trouvez alors devant un bâtiment de pierre blanche qui porte cette
plaque fixée au-dessus de la porte :

**TOUR DE GUET — AUTORITÉ MARITIME**

La rue pavée aboutit à un haut mur de pierre dans lequel est aménagée
une grande porte rouge gardée par deux soldats. Au-delà de cette porte,
on distingue les mâts des navires ancrés dans le port.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans la tour de guet, rendez-vous au :"))
    st.page_link("tomes/tome2/page_318.py", label="318", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous approcher de la porte rouge, rendez-vous au :"))
    st.page_link("tomes/tome2/page_246.py", label="246", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
