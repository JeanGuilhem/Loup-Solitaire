import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=211, book=3)

fr_text = """
Le cyclone est si violent qu'il en déchire presque vos vêtements
tout en vous bombardant de pierres et de morceaux de glace.
Vous serrez les dents et vous essayez de courir, mais le froid
annihile vos forces et vous devez avancer pas à pas en vous
cramponnant au mur pour ne pas être aspiré par le tourbillon
déchaîné.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Si votre total actuel d'ENDURANCE est "
            "inférieur à 10, ôtez 3 points du chiffre que vous aurez tiré. Si le total obtenu est de -3 à 3, "
            "rendez-vous au 95. S'il est de 4 à 9, rendez-vous au 196."
        )
    )
    roll = hazard_roll()
    if roll is not None:
        total = roll
        if st.session_state.endurance < 10:
            total -= 3
            st.write(f"*Votre ENDURANCE est inférieure à 10 : {roll} - 3 = {total}.*")
        if total <= 3:
            st.page_link("tomes/tome3/page_95.py", label="95", icon="📄")
        else:
            st.page_link("tomes/tome3/page_196.py", label="196", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
