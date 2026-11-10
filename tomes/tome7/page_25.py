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

check_inventory(current_page_number=25, book=7)

fr_text = """
Votre sensibilité de Guerrier Kaï vous avertit que cet objet est
maléfique. Sa véritable nature a été habilement dissimulée grâce
à la sorcellerie, mais votre maîtrise des Disciplines Psychiques
vous permet de découvrir le subterfuge : en réalité, ce sceptre
permet à son créateur de prendre le contrôle de quiconque le
touche ou le regarde. Vous sentez une vague de froid envahir
votre cerveau comme si une main glaciale tentait d'écraser votre
volonté, mais vous parvenez à résister à cette attaque grâce à
votre Écran Psychique. D'un brusque coup de pied, vous envoyez
rouler le Sceptre au fond du gouffre. Il se produit un grand
silence, puis une explosion sourde, comme un coup de tonnerre
éloigné, monte des profondeurs insondables jusqu'à vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('A présent, si vous voulez vous engager dans le tunnel est, par lequel les Dhax sont apparus, rendez-vous au :'))
    st.page_link("tomes/tome7/page_185.py", label="185", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous engager dans le tunnel ouest, rendez-vous au :'))
    st.page_link("tomes/tome7/page_308.py", label="308", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
