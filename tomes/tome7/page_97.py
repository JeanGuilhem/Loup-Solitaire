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

check_inventory(current_page_number=97, book=7)

fr_text = """
La créature semble insensible à votre attaque. La vrille s'enroule
solidement autour de votre cou et, d'une brusque secousse, vous
porte à la monstrueuse gueule. Le désespoir l'emporte sur la peur
et la douleur lorsque vous sentez souffler sur votre visage son
haleine tiède et fétide.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    seeds = has_item("GRAINE DE FEU")
    sommerswerd = has_item("GLAIVE DE SOMMER")
    st.write_stream(stream_text("Si vous possédez des Graines de Feu, rendez-vous au :"))
    st.page_link("tomes/tome7/page_10.py", label="10", icon="📄", disabled=not seeds)
    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_317.py", label="317", icon="📄", disabled=not sommerswerd)
    st.write_stream(stream_text("Si vous n'avez ni l'un ni l'autre de ces Objets Spéciaux, rendez-vous au :"))
    st.page_link("tomes/tome7/page_331.py", label="331", icon="📄", disabled=seeds or sommerswerd)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
