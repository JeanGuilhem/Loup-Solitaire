import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=282, book=3)

fr_text = """
Le Barbare des Glaces était armé d'une Lance que vous pouvez
vous approprier si vous le désirez. En fouillant le cadavre, vous
découvrez un étrange Disque de Pierre Bleue. Si vous souhaitez
conserver ce Disque de Pierre Bleue, glissez-le dans votre poche
et inscrivez-le sur votre Feuille d'Aventure, dans la case Objets Spéciaux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("LANCE", key="lance", label="Prendre la Lance")
    if not has_item("DISQUE DE PIERRE BLEUE"):
        pickup_button("DISQUE DE PIERRE BLEUE", key="disque", label="Prendre le Disque de Pierre Bleue")

    st.write_stream(stream_text("Une fois parvenu en haut de l'escalier, vous pouvez prendre à gauche, en direction du nord, en vous rendant au :"))
    st.page_link("tomes/tome3/page_104.py", label="104", icon="📄")

    st.write_stream(stream_text('Si vous préférez prendre à droite en direction du sud, rendez-vous au :'))
    st.page_link("tomes/tome3/page_330.py", label="330", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
