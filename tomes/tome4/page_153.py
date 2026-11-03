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

check_inventory(current_page_number=153, book=4)

fr_text = """
Vous tirez votre flèche qui siffle en direction du chef des bandits,
mais celui-ci la voit et lève son bouclier d'acier. Votre flèche
ricoche sur le métal et vient se fracasser contre le mur de la tour
de guet. Avant que vous n'ayez pu tirer à nouveau, votre arc vous
saute des mains ; c'est un Guerrier en armure qui, d'un violent
coup de pied, vous a ainsi désarmé. Il se tient au-dessus de vous,
debout sur la barricade, et vous ne pouvez éviter son attaque.

Vous aviez remis votre arme au fourreau pour pouvoir faire
usage de votre arc. Malheureusement, le Guerrier bondit sur
vous avant que vous n'ayez pu dégainer à nouveau. Vous n'avez
donc plus d'arme et vous devrez combattre à mains nues pendant
les deux premiers Assauts. De ce fait, vous réduirez de 4 points
votre total d'HABILETÉ. Si lors du troisième Assaut vous êtes
toujours en vie, vous parviendrez à tirer votre arme et votre total
d'HABILETÉ retrouvera son niveau habituel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # les deux premiers Assauts se livrent à mains nues
    outcome = combat([("GUERRIER VASSAGONIEN", 17, 26)], unarmed_rounds=2, potions_allowed=False)
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_174.py", label="174", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
