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
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=321, book=3)

fr_text = """
Vous suivez ce souterrain glacé et sinueux sur plusieurs
kilomètres avant d'arriver enfin dans une grotte. Un petit cours
d'eau coule au milieu de cette caverne et un autre passage permet
de continuer en direction du nord. Lorsque vous sautez le
ruisseau, vous apercevez au fond de l'eau un petit Triangle de
Pierre Bleue accroché à une chaînette. Si vous souhaitez
conserver ce Triangle de Pierre Bleue, passez la chaînette autour
de votre cou et glissez le Triangle sous votre tunique. N'oubliez
pas ensuite d'inscrire l'objet sur votre Feuille d'Aventure dans la
case Objets Spéciaux. Une lumière plus intense éclaire le passage
orienté au nord et vous distinguez au loin une grande caverne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_item("TRIANGLE DE PIERRE BLEUE"):
        pickup_button("TRIANGLE DE PIERRE BLEUE", key="triangle", label="Prendre le Triangle de Pierre Bleue")
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
