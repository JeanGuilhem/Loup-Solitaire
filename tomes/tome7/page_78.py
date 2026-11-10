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

check_inventory(current_page_number=78, book=7)

fr_text = """
Le grand loup bondit sur vous et vous envoie rouler à terre sous
le poids de son énorme masse. Ses griffes vous labourent le bras,
et sa salive brûlante vous éclabousse le visage. Vous vous
défendez de toutes vos forces, avec toute l'habileté dont vous êtes
capable, et vous frappez l'impitoyable bête à grands coups de
couteau, en cherchant à l'atteindre à la gorge. Cette créature est
insensible à la Puissance Psychique, mais non au Foudroiement
Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("LOUP DE LA MORT", 22, 40)], psychic_power_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de ce combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_341.py", label="341", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
