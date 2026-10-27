import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=99, book=2)

fr_text = """
Le lendemain matin, vous êtes réveillé par la vigie postée dans le nid-de-pie.
« Navire par bâbord avant ! » annonce l'homme à grands cris.
Vous grimpez une échelle étroite et vous rejoignez le capitaine qui se
tient à la proue. « Vos yeux sont plus jeunes que les miens, dit-il en
vous tendant une longue-vue ciselée, essayez de voir quel est ce bateau. »
Vous distinguez alors à l'horizon les voiles rouges et le pavillon noir
d'un navire de guerre mené par des pirates Lakuri. Utilisez la Table de
Hasard pour obtenir un chiffre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.write_stream(stream_text("Vous avez tiré un chiffre entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome2/page_326.py", label="326", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Vous avez tiré un 5, un 6, un 7, un 8 ou un 9, rendez-vous au :"))
        st.page_link("tomes/tome2/page_163.py", label="163", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
