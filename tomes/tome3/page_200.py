import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=200, book=3)

fr_text = """
L'effroyable monstre aux longs tentacules surgit du fossé et vous
attaque. Il vous faut le combattre jusqu'à la mort de l'un de vous.
Au cours du combat, vous apercevez parfois Vonotar qui brandit
son bâton noir de magicien en gardant les yeux fixés sur Loi-Kymar.
Il est en train d'attaquer le vieil homme à l'aide de sa
puissante Force Mentale. Et si Loi-Kymar succombe, il
emportera dans la mort le secret de la Crosse de la Guilde.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("AKRANIONOR", 22, 50)], max_rounds=7)
    if outcome == "win":
        st.write_stream(stream_text('Vous avez remporté la victoire en 7 Assauts ou moins, rendez-vous au :'))
        st.page_link("tomes/tome3/page_272.py", label="272", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("S'il vous faut livrer plus de 7 Assauts pour gagner le combat, rendez-vous au :"))
        st.page_link("tomes/tome3/page_324.py", label="324", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
