import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=40, book=6)

fr_text = """
Vous essuyez la lame de votre arme avec le manteau d'un
profanateur de tombes qui gît face contre terre, puis vous
retournez le corps de l'homme du bout de votre botte pour vous
assurer qu'il est bel et bien mort. Aux alentours, plusieurs
sépultures éventrées témoignent de l'odieux forfait des
profanateurs. De la terre fraîchement creusée s'amoncelle à côté
des pierres tombales, et des couvercles de cercueil à demi
fracassés sont éparpillés çà et là, dans le petit cimetière. Les
armes dont ces hommes se sont servis sont tachetées de rouille et
semblent provenir, à l'image de tout le reste du butin, de
tombeaux profanés. En fouillant les dépouilles de vos adversaires,
vous trouvez 27 Pièces d'Or, une Bouteille de Vin et un Miroir.
Prenez les objets qui vous intéressent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(27, key="or_profanateurs")
    pickup_button("BOUTEILLE DE VIN", key="vin", label="Prendre la Bouteille de Vin")
    pickup_button("MIROIR", key="miroir", label="Prendre le Miroir")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
