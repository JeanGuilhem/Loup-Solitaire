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

check_inventory(current_page_number=394, book=5)

fr_text = """
Le Drakkar pousse un cri d'horreur et laisse tomber son épée.
Des milliers d'insectes grouillent sur sa peau qu'ils piquent et
mordent férocement. Le guerrier porte la main à son masque à
tête de mort et essaie fébrilement de relever la visière de son
heaume en métal noir. Dès qu'il y parvient, une nuée
bourdonnante d'insectes s'en échappe. Le Drakkar crie comme
un forcené et, dans un mouvement de panique, bascule par-dessus le parapet et va s'écraser au sol après une chute de
plusieurs centaines de mètres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
