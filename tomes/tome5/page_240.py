import streamlit as st
from combat import combat
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

check_inventory(current_page_number=240, book=5)

fr_text = """
Les Itikars sont des créatures sauvages et rusées de nature. Le
dressage de ces animaux peut prendre plusieurs années, mais
une fois apprivoisés, ces oiseaux noirs géants se montrent des
serviteurs fidèles et dévoués. Alors que vous avancez, l'Itikar sent
que vous n'êtes pas son maître et il vous attaque furieusement
avec son redoutable bec et ses serres acérées.
Menez ce combat de façon normale, mais multipliez par deux
tous les points d'ENDURANCE perdus par l'oiseau géant.
Lorsque son total d'ENDURANCE sera tombé à 0, vous l'aurez
suffisamment maîtrisé pour pouvoir monter en selle et le tenir en
main. Tous les points d'ENDURANCE que vous perdez durant ce
combat compteront pour de véritables blessures et devront par
conséquent être déduits de votre total d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("ITIKAR", 17, 30)], enemy_loss_multiplier=2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous parvenez à réduire le total d'ENDURANCE de l'Itikar à zéro, rendez-vous au :"))
        st.page_link("tomes/tome5/page_217.py", label="217", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
