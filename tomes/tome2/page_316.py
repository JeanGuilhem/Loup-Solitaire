import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=316, book=2)

fr_text = """
Le lendemain matin, vous êtes réveillé par les cris de la vigie postée
dans le nid-de-pie. « Navire en vue par tribord avant ! » annonce-t-il.
Vous montez aussitôt sur le pont en affrontant vaillamment la fraîcheur
de la brise marine. A l'horizon, on aperçoit les rivages boisés qui
s'étendent à l'est du Sommerlund et à mi-chemin, un navire marchand
qui semble sérieusement endommagé. Un seul de ses mâts reste encore
intact et il est de toute évidence en train de sombrer. Le navire bat
pavillon de Durenor, mais le drapeau a été hissé à l'envers en signe de
détresse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome2/page_107.py", label="107", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome2/page_94.py", label="94", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
