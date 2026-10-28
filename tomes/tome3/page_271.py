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

check_inventory(current_page_number=271, book=3)

fr_text = """
Votre attaque a fait perdre l'équilibre à l'éclaireur Barbare qui
tombe en soulevant une gerbe de neige et de débris provenant de
ses skis brisés sous le choc. L'enfant emmitouflé de fourrure est
projeté hors du sac à dos de son père et roule sur lui-même en
venant s'immobiliser face contre terre à moins de 3 mètres de
vous. L'éclaireur Barbare est quelque peu ébranlé par sa chute,
mais il essaie déjà de se relever.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez attaquer l'éclaireur Barbare avant qu'il n'ait complètement repris ses esprits, rendez-vous au :"))
    st.page_link("tomes/tome3/page_241.py", label="241", icon="📄")

    st.write_stream(stream_text("Si vous préférez capturer l'enfant pour le prendre en otage et tenter ainsi de vous échapper, rendez-vous au :"))
    st.page_link("tomes/tome3/page_262.py", label="262", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
