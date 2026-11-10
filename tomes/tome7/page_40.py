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

check_inventory(current_page_number=40, book=7)

fr_text = """
Le garde secoue la corde et, aussitôt, le tintement agressif d'une
cloche d'alarme emplit le couloir. D'autres gardes en armure font
irruption, l'arme au poing et la visière baissée, prêts à combattre.
Ils vous repèrent immédiatement et se ruent sur vous. Ils vous
attaquent tous les quatre en même temps et vous devrez les
combattre comme s'ils ne faisaient qu'un :
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("RAKHOS DE ZAHDA", 30, 39)], max_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text('Si vous sortez vainqueur de cet affrontement en 3 Assauts ou moins, rendez-vous au :'))
        st.page_link("tomes/tome7/page_248.py", label="248", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text('Si le combat dure plus de 3 Assauts, rendez-vous au :'))
        st.page_link("tomes/tome7/page_160.py", label="160", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
