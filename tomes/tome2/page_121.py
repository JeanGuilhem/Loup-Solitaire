import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=121, book=2)

fr_text = """
Vous courez le long de la rue de la Vigie et vous atteignez bientôt le
quai, là où le fleuve Dorn sépare les parties Est et Ouest de la ville. A
votre gauche, vous apercevez le pont de Ragadorn, un ouvrage d'une
grande laideur dont le fer a rouillé et qui constitue le seul point de
passage entre les deux moitiés de Ragadorn. Les cris des voleurs
retentissent encore à vos oreilles tandis que vous vous frayez un chemin
parmi la foule qui encombre le pont. Mais, lorsque vous êtes parvenu
de l'autre côté, les voleurs ont abandonné la poursuite et vous vous
engagez dans une large avenue qui porte le nom de boulevard du
Commerce, section Est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
