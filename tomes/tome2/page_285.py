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

check_inventory(current_page_number=285, book=2)

fr_text = """
Vous sentez les crochets du serpent s'enfoncer dans la manche de votre
tunique, mais rien de plus. Vous avez de la chance : seul votre vêtement
a souffert de la morsure. Le serpent s'enfuit aussitôt et disparaît dans
l'herbe haute ; vous vous hâtez alors de grimper à l'arbre pour passer le
reste de la nuit à l'abri de son feuillage, à bonne distance du sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
