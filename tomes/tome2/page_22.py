import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=22, book=2)

fr_text = """
Au matin, vous êtes réveillé par un cri de l'homme de quart : « Naufrage par tribord avant ! » Vous vous habillez en hâte et vous
montez sur le pont pour rejoindre le capitaine qui se tient debout devant
le bastingage de la proue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez 0, 1, 2, 3 ou 4, rendez-vous au 119. Si vous tirez 5, 6, 7, 8 ou 9, rendez-vous au 341."))
    number = hazard_roll()
    if number is not None and 0 <= number <= 4:
        st.page_link("tomes/tome2/page_119.py", label="119", icon="📄")
    elif number is not None and 5 <= number <= 9:
        st.page_link("tomes/tome2/page_341.py", label="341", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
