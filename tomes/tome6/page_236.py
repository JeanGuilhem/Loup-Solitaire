import streamlit as st
from inventory import (
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

check_inventory(current_page_number=236, book=6)

fr_text = """
La flèche siffle dans l'obscurité et arrache une touffe de fourrure
et un morceau de peau du crâne de la créature. Celle-ci pousse
un cri de douleur et porte la patte à sa blessure. Mais, bien
qu'atteint à la tête, le monstre est loin d'être mort et il passe à
l'attaque en lançant sa patte sanglante aux griffes acérées vers
votre tête. Vous plongez juste à temps pour éviter d'être décapité.
Vous vous redressez et vous vous préparez à un combat au corps
à corps avant que le monstre passe de nouveau à l'attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_343.py", label="343", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
