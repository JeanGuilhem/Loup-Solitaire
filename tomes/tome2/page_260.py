import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=260, book=2)

fr_text = """
Le capitaine ordonne qu'on mette le cap sur les trois hommes et qu'on
les hisse à bord. Ce sont des pêcheurs de Tyso, un port du Sommerlund.
Leur bateau a été attaqué par des pirates la nuit précédente et ils sont
les seuls survivants. Vous leur donnez à manger et des vêtements
chauds ; les trois hommes alors retiennent leurs larmes à grand peine et
l'un d'eux vous fait présent d'une magnifique Epée en témoignage de sa
reconnaissance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez accepter ce cadeau, n'oubliez pas de l'inscrire sur votre Feuille d'Aventure."))
    pickup_button("ÉPÉE", key="epee", label="Accepter l'Épée")

    st.write_stream(stream_text('Rendez-vous ensuite au :'))
    st.page_link("tomes/tome2/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
