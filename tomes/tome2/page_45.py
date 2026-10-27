import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=45, book=2)

fr_text = """
Vous galopez le long du chemin forestier en direction des cavaliers
vêtus de capes ; soudain, l'un d'eux lève un épieu de couleur noire au-
dessus de sa tête. A l'extrémité de l'épieu est fixé un cône d'acier, noir
également, d'où s'échappe une flamme bleue étincelante. Vous vous
apprêtez à porter votre premier coup lorsqu'un éclair aveuglant jaillit du
bâton maléfique et explose juste à côté de vous. La force de la
déflagration est telle que vous êtes projeté à terre dans les broussailles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez un chiffre de 0 à 7, rendez-vous au 311. Si vous tirez un 8 ou un 9, rendez-vous au 159."))
    number = hazard_roll()
    if number is not None and 0 <= number <= 7:
        st.page_link("tomes/tome2/page_311.py", label="311", icon="📄")
    elif number is not None and 8 <= number <= 9:
        st.page_link("tomes/tome2/page_159.py", label="159", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
