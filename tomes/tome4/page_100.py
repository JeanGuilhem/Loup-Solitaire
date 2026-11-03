import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=100, book=4)

fr_text = """
Un sentiment de répulsion vous envahit, tandis que vous
contemplez l'autel et le sanctuaire du temple souterrain. Votre
sensibilité de Seigneur Kaï semble s'enflammer comme si chaque
nerf de votre corps vous incitait à fuir ces lieux maléfiques.
D'immenses braseros de métal fondu entourent un autel noir sur
lequel est étendue la blonde Madelon, fille du baron Vanalund.
Elle paraît plongée dans une transe profonde ; sa respiration est
lente et brève. De l'autre côté de l'autel, vous apercevez deux
portes massives de pierre noire ; chacune est gravée d'une
gigantesque tête de mort. Dans un autre coin du temple, hors de
vue pour l'instant, une troisième porte s'ouvre et une procession
de prêtres vêtus de capes rouges fait son entrée. Ils ont la tête
encapuchonnée et chacun porte dans ses mains tendues
d'étranges Amulettes. Ils défilent devant l'autel, déposent leurs
Amulettes en cercle autour du corps de la jeune fille puis
s'éloignent dans un silence total. Quelques instants plus tard,
vous entendez le son d'un battement de tambour dont l'intensité
augmente régulièrement. Des bruits de pas cadencés produits
par des bottes aux semelles ferrées résonnent à sa suite. Barraka
s'approche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
