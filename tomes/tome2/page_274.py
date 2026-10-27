import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=274, book=2)

fr_text = """
En fouillant rapidement les corps, vous trouvez une Épée, 6 Pièces d'Or
et une Masse d'Armes. Emportez ce que vous voulez le cas échéant,
sans oublier de modifier en conséquence votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_gold(6, key="gold")
    pickup_button("MASSE D'ARMES", key="masse", label="Prendre la Masse d'Armes")

    st.write_stream(stream_text("Avant que vous ayez eu le temps de sortir par la porte de devant, d'autres villageois furieux ont réussi à pénétrer dans la boutique et vous devez à présent vous enfuir par la fenêtre du premier étage. Rendez-vous au :"))
    st.page_link("tomes/tome2/page_132.py", label="132", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
