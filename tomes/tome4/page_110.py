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

check_inventory(current_page_number=110, book=4)

fr_text = """
Vous ouvrez d'un coup de pied la porte de la roulotte et vous vous
précipitez à l'intérieur. Malheureusement, vous n'y trouvez pas
l'acteur, mais une jeune femme en train de prendre son bain.
Après quelques secondes d'un silence stupéfait, la femme se met
à hurler à pleins poumons, ne s'interrompant que pour vous jeter
à la tête tout ce qui lui tombe sous la main. Sous une pluie de
brosses, de miroirs, de peignes et de jurons, vous êtes expulsé de
la roulotte dont la porte se referme brutalement sur vous. Au-dehors,
vous vous retrouvez face à un petit groupe de gens que le
vacarme a attirés. Aucune des personnes présentes ne parlant ou
ne comprenant le sommerlundais, vous êtes dans l'impossibilité
d'expliquer votre innocente erreur. Considérant les regards
hostiles qui sont fixés sur vous, vous estimez préférable de
renoncer à chercher l'acteur en fuite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_165.py", label="165", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
