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

check_inventory(current_page_number=336, book=4)

fr_text = """
La flèche siffle droit vers le brigand mais elle ricoche sur son
plastron d'acier. Sans être le moins du monde ému par le choc,
l'homme lance son javelot, transperçant le malheureux soldat.
Vous vous apprêtez à tirer une autre flèche, lorsqu'une forme
noire et menaçante apparaît soudain dans le ciel. Cette silhouette
fond sur la tour au sommet de laquelle elle atterrit. Vous jetez
alors votre arc, vous dégainez votre arme et vous montez les
marches quatre à quatre pour aller voir de quoi il retourne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_223.py", label="223", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
