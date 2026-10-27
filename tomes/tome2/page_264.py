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

check_inventory(current_page_number=264, book=2)

fr_text = """
Vous concentrez toute l'énergie de votre pouvoir sur le reptile et vous
lui ordonnez de partir à l'instant en quête d'une proie. Lentement, votre
puissance de suggestion fait son effet et le serpent s'éloigne enfin, puis
disparaît dans les hautes herbes. Vous poussez un soupir de
soulagement et, pour plus de sûreté, vous grimpez à l'arbre où vous
passerez le reste de la nuit à l'abri du feuillage et à bonne distance du
sol.
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
