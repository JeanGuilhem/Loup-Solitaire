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

check_inventory(current_page_number=290, book=7)

fr_text = """
Vous le suivez jusqu'au bout du couloir et vous entendez derrière
vous les cris de colère des geôliers de Zahda. Vous arrivez en haut
d'un escalier qui descend au niveau inférieur, mais il est gardé
par un Rakhos à la gueule menaçante, armé d'une hache.
Doublez tous les points d'ENDURANCE perdus par votre
ennemi, car le Rakhos subit également l'assaut de votre nouveau
partenaire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GEÔLIER RAKHOS", 17, 22)], enemy_loss_multiplier=2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_220.py", label="220", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
