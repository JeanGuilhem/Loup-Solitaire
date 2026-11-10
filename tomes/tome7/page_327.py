import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    magnakai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=327, book=7)

fr_text = """
Vous aspirez une grande bouffée d'air et plongez. Vous
concentrez votre Pouvoir Magnakaï sur la serrure et essayez de
l'ouvrir. C'est un test difficile pour votre habileté, rendu plus
malaisé encore par le manque d'air.
Utilisez la Table de Hasard pour obtenir un chiffre. Si vous avez atteint le rang de Maître primat, ajoutez 2 au chiffre obtenu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll(key="serrure")
    if roll is not None:
        bonus = 2 if magnakai_rank() >= 4 else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Rang de Maître primat : {roll} + 2 = **{total}**.*")
        st.write_stream(stream_text("Si votre total est inférieur ou égal à 4, rendez-vous au :"))
        st.page_link("tomes/tome7/page_184.py", label="184", icon="📄", disabled=total > 4)
        st.write_stream(stream_text("S'il est supérieur ou égal à 5, rendez-vous au :"))
        st.page_link("tomes/tome7/page_4.py", label="4", icon="📄", disabled=total <= 4)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
