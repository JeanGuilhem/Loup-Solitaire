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

check_inventory(current_page_number=225, book=5)

fr_text = """
L'homme est de petite stature, mais large d'épaules et solidement
bâti, selon les caractéristiques physiques communes au rudes
montagnards de Vassagonie. Il débouche une bouteille de vin
vert clair puis il en verse trois grandes rasades dans les coupes en
terre. « Kourshah ! » s'écrie-t-il, puis il vide sa coupe d'un trait.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez l'imiter et boire ce vin mystérieux, rendez-vous au :"))
    st.page_link("tomes/tome5/page_211.py", label="211", icon="📄")

    st.write_stream(stream_text("Si vous ne voulez pas en boire, demandez-lui où vous pouvez trouver Tipasa et rendez-vous au :"))
    st.page_link("tomes/tome5/page_318.py", label="318", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
