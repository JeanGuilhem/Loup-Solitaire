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

check_inventory(current_page_number=332, book=4)

fr_text = """
Bien que les roulottes soient plongées dans l'obscurité, vos sens
aigus de Seigneur Kaï vous révèlent la cachette de l'acteur. Vous
montez alors les quelques marches qui mènent à la porte arrière
d'une grande roulotte, vous poussez le panneau à l'aide de votre
arme et vous entrez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_222.py", label="222", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
