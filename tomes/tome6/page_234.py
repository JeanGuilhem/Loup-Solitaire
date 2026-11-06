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

check_inventory(current_page_number=234, book=6)

fr_text = """
Une voix vous parvient du casque noir en acier : « Ta dernière
heure a sonné, habitant du Nord ! » Le guerrier surgit de la Porte
de Denka, jette son arbalète et se précipite sur vous en
brandissant une hache. Vous ne pouvez pas éviter l'affrontement,
et le combat devra se poursuivre jusqu'à la mort. Étant donné la
rapidité de l'attaque de votre adversaire, vous ne pouvez pas
utiliser d'Arc.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("ASSASSIN À L'ARMURE", 24, 26)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome6/page_28.py", label="28", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
