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

check_inventory(current_page_number=178, book=2)

fr_text = """
Bien que la délicieuse odeur de cette nourriture vous fasse saliver, vous
soupçonnez quelque chose de louche et vous posez le plateau à terre,
près de la porte. Vous êtes fatigué à force d'avoir faim et vous décidez
de faire un somme avant d'aller rejoindre les autres au bar. Lorsque
vous vous réveillez, vous apercevez les cadavres de deux rats étendus
près du plateau : ils sont morts empoisonnés. Vous êtes alors saisi de
fureur, car c'est à vous que cette nourriture était destinée. Vous vous
hâtez de ramasser vos affaires et vous quittez la chambre, bien décidé à
retrouver celui ou celle qui a tenté de vous assassiner.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
