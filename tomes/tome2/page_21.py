import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    receive_gold,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=21, book=2)

fr_text = """
Le tricheur est étendu raide mort à vos pieds. Vous retournez son
cadavre, puis vous ôtez des manches de sa veste plusieurs cartes qu'il
cachait là. Vous les jetez sur la table et bientôt la foule se disperse dans
la taverne qui retrouve instantanément son vacarme et son agitation
habituels. Les autres joueurs de cartes récupèrent leur or et vous
laissent ce qui reste.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Pour savoir quelle quantité d'or vous revient, utilisez la Table de Hasard en remplaçant exceptionnellement le zéro par le chiffre 10. Lorsque la Table vous aura donné un chiffre, vous le multiplierez par 3 ; le total obtenu représente le nombre de Pièces d'Or qui vous appartient désormais."))
    roll = hazard_roll()
    if roll is not None:
        value = roll if roll != 0 else 10
        receive_gold(value * 3)
        st.write_stream(stream_text("Vous pouvez également prendre le Poignard si vous le désirez."))
        pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
        st.write_stream(stream_text("Tandis qu'on enlève le cadavre du tricheur, vous vous approchez du bar et vous appelez l'aubergiste, puis vous lui glissez une Pièce d'Or dans le creux de la main en lui demandant une chambre pour la nuit."))
        if "hazard_room_paid" not in st.session_state:
            spend_gold(1)
            st.session_state["hazard_room_paid"] = True
        st.caption("Vous avez payé 1 Couronne pour la chambre.")
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("tomes/tome2/page_314.py", label="314", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
