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

check_inventory(current_page_number=255, book=5)

fr_text = """
Tandis que le Drakkar s'effondre au sol, un Cube en Cristal noir
tombe de sa poche. Si vous souhaitez prendre cet objet, placez-le
dans votre poche et inscrivez-le sur votre Feuille d'Aventure dans
la case des Objets Spéciaux. Soudain le cri aigu des Vordaks vous
éloigne du cadavre. Ce cri hideux vous perce les tympans et se
rapproche dangereusement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("CUBE DE CRISTAL NOIR", key="cube", label="Prendre le Cube en Cristal noir")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_228.py", label="228", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
