import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=290, book=5)

fr_text = """
Vous fouillez le corps du chef des Drakkars, et vous découvrez
dans sa poche un Cube en Cristal noir. Si vous souhaitez garder
ce Cube en Cristal noir, mettez-le dans votre poche, et notez-le
sur votre Feuille d'Aventure dans la case des Objets Spéciaux.
Mais le bruit d'autres Drakkars descendant l'escalier de la tour
vient interrompre vos recherches et vous vous précipitez vers la
porte en bois.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("CUBE DE CRISTAL NOIR", key="cube", label="Garder le Cube en Cristal noir")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_246.py", label="246", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
