import streamlit as st
from inventory import (
    buy_button,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=327, book=2)

fr_text = """
Vous rebroussez chemin le long de la rue pavée en vous demandant ce
qu'il convient de faire lorsqu'un jeune garçon s'approche de vous. «Je
peux vous faire entrer dans le port, dit-il, mais il faudra payer. » Il vous
montre alors une enveloppe remplie de papiers officiels ou qui
semblent tels. « Grâce à ces papiers, poursuit-il, vous obtiendrez un
laissez-passer rouge au poste de garde du port. Ils sont à vous pour 6
Couronnes seulement. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez acheter ces documents, payez-les 6 Couronnes."))
    buy_button("DOCUMENTS", 6, key="documents", label="Acheter les documents (6 Couronnes)")
    st.write_stream(stream_text("Si vous refusez, le garçon vous laisse là et disparaît bientôt. Lorsque vous aurez pris une décision, vous retournerez à la tour."))
    st.write_stream(stream_text("Si vous souhaitez y entrer, rendez-vous au :"))
    st.page_link("tomes/tome2/page_318.py", label="318", icon="📄")
    st.write_stream(stream_text("Si vous préférez emprunter l'avenue bordée d'arbres pour retourner à l'hôtel de ville et y demander comment faire pour vous rendre au Consulat du Sommerlund, rendez-vous au :"))
    st.page_link("tomes/tome2/page_84.py", label="84", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
