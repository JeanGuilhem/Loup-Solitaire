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

check_inventory(current_page_number=243, book=3)

fr_text = """
Vous bénéficiez d'une chance exceptionnelle. Vous avez en effet
évité de justesse une crevasse profonde que l'obscurité vous
cachait. Vous poursuivez donc votre chemin en direction de la
lueur sans vous préoccuper des bleus et contusions qui se
multiplient sur vos tibias et vos genoux à mesure que vous vous
cognez contre les blocs de glace dressés sur votre passage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
