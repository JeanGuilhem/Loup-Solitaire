import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=332, book=2)

fr_text = """
Il vous faut à présent combattre le MONSTRE D'ENFER.
Il vous attaque en faisant usage de sa Puissance Psychique et si vous ne
maîtrisez pas la Discipline Kaï du Bouclier Psychique, vous perdrez 2
points d'ENDURANCE supplémentaire au cours de chaque assaut.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez prendre la fuite à tout moment en vous réfugiant dans la forêt."))
    outcome = combat([("MONSTRE D'ENFER", 21, 30)], flee_after=0, psychic_damage=2, undead=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome2/page_92.py", label="92", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous vous réfugiez dans la forêt, rendez-vous au :"))
        st.page_link("tomes/tome2/page_183.py", label="183", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
