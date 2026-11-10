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

check_inventory(current_page_number=70, book=7)

fr_text = """
Le Zagothal est aveugle et complètement sourd. Grâce à votre
talent de Maître Kaï, vous parvenez à masquer l'odeur et la
chaleur de votre corps, et à esquiver ainsi son attaque avant de
prendre la fuite. Une fois arrivé au pied de la paroi rocheuse,
vous découvrez une grande fissure qui déchire verticalement le
noir rocher. Mais au moment même où vous vous apprêtez à y
pénétrer, vous entendez à l'intérieur des bruits étranges qui vous
font quelque peu hésiter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez malgré tout entrer dans cette faille, rendez-vous au :"))
    st.page_link("tomes/tome7/page_16.py", label="16", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer le long de la plage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_173.py", label="173", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
