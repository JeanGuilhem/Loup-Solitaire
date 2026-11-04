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

check_inventory(current_page_number=382, book=5)

fr_text = """
Brusquement, le Drakkar se met à crier en agitant les bras, ses
mains gantées s'ouvrant et se fermant convulsivement. Il est la
proie de quelque pouvoir invisible qui est en train de le tuer au
sein même de son armure. Vous reculez tandis que le bruit
affreux des os qui se brisent s'élève au-dessus des cris stridents
des Kraans qui fondent sur le vaisseau. Le Drakkar trébuche sur
le pont puis bascule par-dessus le bord de la plate-forme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_294.py", label="294", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
