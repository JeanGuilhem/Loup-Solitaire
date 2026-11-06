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

check_inventory(current_page_number=308, book=6)

fr_text = """
Votre Discipline Magnakaï vous permet de comprendre la
signification du symbole gravé dans la pierre au-dessus de la
porte sud. C'est un éperon ailé, emblème de l'Armée de Lyris.
Cette porte doit mener à une salle de garde car la route qui y
mène ne montre que des empreintes de chevaux ferrés. L'autre
route, en revanche, est pleine d'ornières creusées par les roues
des chariots, car c'est par la porte nord que s'effectue l'important
trafic de marchandises entre Quarlen et Casiorn. De plus, les
gardes-frontières de Lyris ont la réputation d'être très peu
amicaux et il serait plus sage de les éviter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez avancer vers la porte nord, rendez-vous au :'))
    st.page_link("tomes/tome6/page_137.py", label="137", icon="📄")

    st.write_stream(stream_text('Si vous préférez avancer vers la porte sud, rendez-vous au :'))
    st.page_link("tomes/tome6/page_225.py", label="225", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
