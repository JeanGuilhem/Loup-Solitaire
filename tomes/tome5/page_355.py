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

check_inventory(current_page_number=355, book=5)

fr_text = """
Vous roulez sur le côté, une fraction de seconde avant que la
masse ne s'écrase au sol, à l'endroit précis où se trouvait votre
tête. A moins que vous ne maîtrisiez la Discipline Kaï du Bouclier
Psychique, diminuez de 2 points votre total d'HABILETÉ pour
toute la durée du combat, car le Vordak utilise sa force psychique
contre vous. Lui, en revanche, est insensible à la puissance psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VORDAK", 17, 26)], psychic_attack=True, psychic_immune=True, max_rounds=4)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat en 4 Assauts, ou moins, rendez-vous au :"))
        st.page_link("tomes/tome5/page_249.py", label="249", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("Si le combat dure plus de 4 Assauts, rendez-vous au :"))
        st.page_link("tomes/tome5/page_304.py", label="304", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
