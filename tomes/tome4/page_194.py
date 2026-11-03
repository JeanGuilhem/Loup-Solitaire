import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=194, book=4)

fr_text = """
Vous êtes projeté dans l'eau glacée par le tentacule qui vous
frappe en pleine poitrine. Vous refaites rapidement surface mais
vous avez à peine le temps de respirer une bouffée d'air qu'un
autre tentacule s'enroule autour de vos jambes et vous attire vers
le fond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre (exceptionnellement 0 = 10). Ce chiffre représente le nombre d'Assauts que vous pourrez livrer sous l'eau avant de perdre des points d'ENDURANCE supplémentaires en raison du manque d'oxygène. Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, vous ajouterez 2 au chiffre donné par la Table."))
    roll = hazard_roll(key="oxygene")
    if roll is not None:
        limit = roll if roll != 0 else 10
        if has_kai("Maîtrise Psychique de la Matière"):
            limit += 2
            st.write(f"*Maîtrise Psychique de la Matière : +2, soit {limit} Assauts.*")
        st.write(f"*Vous pouvez livrer {limit} Assauts sous l'eau avant de manquer d'oxygène.*")
        st.write(
            "Affrontez à présent ce Mégacalmar. Vous engagerez ce combat à la manière habituelle. "
            "S'il comporte un nombre d'Assauts supérieur au chiffre que vous aurez tiré, vous perdrez "
            "2 points d'ENDURANCE en plus à chaque Assaut supplémentaire. C'est ce que vous coûte le "
            "manque d'oxygène."
        )
        # manque d'oxygène : -2 ENDURANCE à chaque Assaut au-delà de `limit`
        outcome = combat([("MÉGACALMAR", 16, 37)], extra_loss=2, extra_loss_after=limit)
        if outcome == "win":
            st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
            st.page_link("tomes/tome4/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
