import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=111, book=2)

fr_text = """
A contrecœur, les gardes baissent les armes et vous autorisent à
franchir le pont. Au moment où vous passez devant eux, ils vous fixent
du regard puis se chuchotent quelques mots à l'oreille. Dès que vous
avez franchi le chenal de Ryner, vous vous hâtez de poursuivre votre
chemin, de peur qu'ils ne changent d'avis et vous arrêtent. Au bout
d'une heure de marche sur la route qui traverse la forêt, vous arrivez à
un croisement où un poteau de signalisation indique la direction de l'est
: PORT BAX 5 km. Vous souriez et vous suivez la flèche : dans une
heure tout au plus, vous devriez être arrivé à destination.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_265.py", label="265", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
