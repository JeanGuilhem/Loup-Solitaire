import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=186, book=3)

fr_text = """
Le fils du Barbare mort s'agenouille devant le cadavre de son
père et pose sur vous un regard brillant de haine. Pendant ce
temps, les autres éclaireurs Barbares s'approchent de vous et il
vous faut agir vite si vous voulez leur échapper. Vous décidez
alors de prendre l'enfant en otage, mais il se débat comme un
animal sauvage : il mord, griffe et donne des coups de pied pour
essayer de se dégager.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_320.py", label="320", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
