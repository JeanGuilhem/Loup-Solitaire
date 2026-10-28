import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=294, book=3)

fr_text = """
Abattre la porte de cette façon représente une tâche harassante
qui vous demandera six heures d'effort. Lorsque vous serez
arrivé au bout de vos peines, il vous faudra prendre 2 Repas,
sinon, vous perdrez 6 points d'ENDURANCE en raison de la
fatigue. Quand enfin vous aurez réussi à creuser un trou
suffisamment large pour vous permettre de passer, vous vous
rendrez compte que vous avez malencontreusement attiré
l'attention de quelqu'un.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()
    handle_repas()

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_106.py", label="106", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
