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

check_inventory(current_page_number=47, book=4)

fr_text = """
Vous parvenez à aspirer une bouffée d'air avant que l'eau sombre
ne se referme sur vous. Un tentacule vous effleure le pied et vous
lui portez un coup, l'empêchant ainsi de s'enrouler autour de
votre jambe. La créature est à présent gravement blessée, ce qui
la rend d'autant plus acharnée à vous faire payer de votre vie la
douleur que vous lui avez infligée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("MÉGACALMAR", 16, 37)], max_rounds=5)
    if outcome == "rounds_over":
        st.write_stream(stream_text("Le combat dure plus de 5 Assauts, rendez-vous au :"))
        st.page_link("tomes/tome4/page_340.py", label="340", icon="📄")

    elif outcome == "win":
        st.write_stream(stream_text("Vous remportez la victoire en 5 Assauts ou moins, rendez-vous au :"))
        st.page_link("tomes/tome4/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
