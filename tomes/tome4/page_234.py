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

check_inventory(current_page_number=234, book=4)

fr_text = """
Vous avez à peine eu le temps de respirer une bouffée d'air qu'un
tentacule s'enroule autour de vos jambes et vous attire vers le
fond. Utilisez la Table de Hasard pour obtenir un chiffre et notez
ce chiffre dans la marge de votre Feuille d'Aventure
(exceptionnellement 0 = 10). Ce chiffre représente le nombre
d'Assauts que vous pourrez livrer sous l'eau avant de perdre des
points d'ENDURANCE supplémentaires en raison du manque
d'oxygène. Si vous possédez la Discipline Kaï de la Maîtrise
Psychique de la Matière, vous ajouterez 2 au chiffre que vous
aurez tiré. Engagez à présent le combat avec le Mégacalmar.
Vous mènerez ce combat à la manière habituelle. Mais, s'il dure
au-delà du nombre d'Assauts correspondant au chiffre que vous
aurez tiré, vous perdrez 2 points d'ENDURANCE à chaque
nouvel Assaut supplémentaires. C'est le prix que vous coûte le
manque d'oxygène.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None:
        value = roll if roll != 0 else 10
        breath = value + (2 if has_kai("Maîtrise Psychique de la Matière") else 0)
        if has_kai("Maîtrise Psychique de la Matière"):
            st.write(f"*Maîtrise Psychique de la Matière : +2, soit {breath} Assauts.*")
        st.info(f"Vous pouvez livrer {breath} Assauts sous l'eau avant de manquer d'oxygène.")
        # manque d'oxygène : -2 ENDURANCE à chaque Assaut au-delà de `breath`
        outcome = combat([("MÉGACALMAR", 16, 37)], extra_loss=2, extra_loss_after=breath)
        if outcome == "win":
            st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
            st.page_link("tomes/tome4/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
