import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=301, book=2)

fr_text = """
En fouillant les cadavres, vous trouvez 3 Pièces d'Or, 3 Poignards et 1
Sabre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write("Vous pouvez emporter l'un ou l'autre de ces objets :")
    pickup_gold(3, key="gold")
    pickup_button("POIGNARD", key="poignard_1", label="Prendre un Poignard")
    pickup_button("POIGNARD", key="poignard_2", label="Prendre un deuxième Poignard")
    pickup_button("POIGNARD", key="poignard_3", label="Prendre un troisième Poignard")
    pickup_button("SABRE", key="sabre", label="Prendre le Sabre")

    st.write_stream(stream_text("Rendez-vous ensuite au :"))
    st.page_link("tomes/tome2/page_20.py", label="20", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
