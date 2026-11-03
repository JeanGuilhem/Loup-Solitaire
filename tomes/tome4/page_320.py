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

check_inventory(current_page_number=320, book=4)

fr_text = """
Votre attaque prend les deux Gardes complètement au dépourvu.
Ils ont à peine eu le temps de tirer leur épée que vos hommes les
projettent tous deux à terre, leurs armes levées au-dessus de leur
tête. « Faut-il les exécuter à l'instant, Seigneur Kaï ? » demande
un patrouilleur en appuyant la pointe de son épée sur la gorge de
l'un des gardes. « Non, répondez-vous, attachez-les plutôt, ils
peuvent peut-être nous être utiles. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez fouiller les Gardes, rendez-vous au :"))
    st.page_link("tomes/tome4/page_268.py", label="268", icon="📄")

    st.write_stream(stream_text("Si vous préférez les interroger, rendez-vous au :"))
    st.page_link("tomes/tome4/page_76.py", label="76", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
