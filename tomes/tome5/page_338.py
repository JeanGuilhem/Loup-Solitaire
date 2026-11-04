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

check_inventory(current_page_number=338, book=5)

fr_text = """
Utilisant la technique de combat à mains nues que vous ont
enseignée les Maîtres Kaï, vous saisissez le Garde à la gorge et
vous le projetez violemment par-dessus le muret de pierre qui
borde le palier. L'homme tombe dans le vide en poussant un
effroyable cri d'horreur avant de s'écraser sur les dalles de pierre
en contrebas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez continuer à monter l'escalier jusqu'à la porte qui donne accès au chemin de ronde, rendez-vous au :"))
    st.page_link("tomes/tome5/page_372.py", label="372", icon="📄")

    st.write_stream(stream_text("Si vous préférez entrer par la porte d'où le Garde avait surgi, rendez-vous au :"))
    st.page_link("tomes/tome5/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
