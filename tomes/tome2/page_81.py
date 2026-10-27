import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=81, book=2)

fr_text = """
Le lendemain matin, vous êtes réveillé par la vigie postée dans le nid-de-pie :
« Canot de sauvetage sur bâbord avant», annonce l'homme à
grands cris. Vous montez sur le pont en affrontant la fraîcheur de la
brise et vous y rencontrez le capitaine. A une cinquantaine de mètres
sur bâbord avant, un canot endommagé dérive, ballotté par une forte
houle. A bord, trois hommes serrés les uns contre les autres essaient de
se protéger de la froideur du vent. Utilisez la Table de Hasard pour
obtenir un chiffre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.write_stream(stream_text("Vous avez tiré entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome2/page_260.py", label="260", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Vous avez tiré entre 5 et 9, rendez-vous au :"))
        st.page_link("tomes/tome2/page_281.py", label="281", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
