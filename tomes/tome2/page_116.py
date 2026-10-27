import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    receive_gold,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=116, book=2)

fr_text = """
Grâce à la Discipline Kaï, vous n'avez aucune difficulté à découvrir
sous quelle tasse la bille est cachée, car pour vous l'argile est aussi
transparente que le verre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre et ajoutez-y 5. Vous saurez ainsi combien de Pièces d'Or vous avez gagnées avant que le fripon vous soupçonne et mette fin au jeu."))
    number = hazard_roll()
    if number is not None:
        receive_gold(number + 5)
        if not st.session_state.get("visibility_room_116"):
            # le prix de la chambre, payé une seule fois par visite
            st.session_state["visibility_room_116"] = True
            spend_gold(1)
        st.write_stream(stream_text("Votre bourse est à nouveau remplie et vous retournez au bar où vous payez le prix d'une chambre, soit une Pièce d'Or. Rendez-vous au :"))
        st.page_link("tomes/tome2/page_314.py", label="314", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
