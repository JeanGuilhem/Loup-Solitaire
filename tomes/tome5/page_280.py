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

check_inventory(current_page_number=280, book=5)

fr_text = """
Le Drakkar est en train d'étrangler le Nain. Lorsqu'il vous
aperçoit, il relâche sa prise, puis écrase son poing ganté de fer sur
la figure du Nain qui s'écroule au sol. Ce meurtre de sang-froid
vous fait bouillonner d'indignation et de rage ! Vous tirez votre
arme et vous passez aussitôt à l'attaque.
La rapidité de votre attaque vous permet de ne déduire aucun
point d'ENDURANCE pendant le premier Assaut.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DRAKKAR", 18, 25)], ls_immune_rounds=1)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_213.py", label="213", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
