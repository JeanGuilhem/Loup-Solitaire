import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=130, book=2)

fr_text = """
Le moine qui voyageait en votre compagnie dans la diligence s'est
approché de vous. « Vous avez besoin de vous reposer, comme nous
tous, dit-il, je comprends votre embarras, mon fils; aussi permettez-moi
de mettre en pratique ce que je m'efforce de prêcher. » Il vous conduit
alors au bar puis dépose une Pièce d'Or dans la main de l'aubergiste. «
Veuillez donner une chambre à mon ami », dit-il avec un sourire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_314.py", label="314", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
