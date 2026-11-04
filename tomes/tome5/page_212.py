import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=212, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
A travers l'épais rideau d'arbres, vous apercevez des ombres
fugitives : ce sont les Drakkars qui tentent de vous encercler.
Soudain, une forme rouge surgit du feuillage et une masse
d'armes vous frôle la tête. La puissance du coup vous envoie
rouler au sol comme si la masse vous avait touché. Le Vordak
éclate d'un rire maléfique et se précipite sur vous, en brandissant
son arme noire pour vous fracasser le crâne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome5/page_349.py", label="349", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_349.py", label="349", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome5/page_355.py", label="355", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_355.py", label="355", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
