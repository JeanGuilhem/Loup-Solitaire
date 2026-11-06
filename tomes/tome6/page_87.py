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

check_inventory(current_page_number=87, book=6)

fr_text = """
Les gardes de la ville se précipitent pour venger leur sergent
mais, dans leur hâte, ils laissent un passage libre entre deux
chariots. Vous saisissez immédiatement l'occasion pour éperonner
votre cheval et vous lancer à la rencontre des soldats qui
accourent vers vous en brandissant leurs armes. Mais ces jeunes
recrues n'ont que peu d'expérience au combat : elles sont
malhabiles et hésitantes, et vous vous débarrassez d'elles en
quelques secondes. Puis vous vous élancez entre les deux
chariots et vous vous éloignez au triple galop.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
