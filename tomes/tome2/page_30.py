import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=30, book=2)

fr_text = """
Vous tombez sur les planches moisies du pont et vous passez au travers
pour atterrir enfin au fond d'une cale. Vous êtes indemne, mais la
puanteur dans laquelle baigne le navire est insupportable. Vous vous
remettez sur pied et vous dégainez le Glaive de Sommer. Quatre
ZOMBIES aux allures de fantômes sortent alors de l'ombre d'un pas
chancelant en tendant vers votre gorge des mains noueuses et
décharnées. Il vous faut les combattre en les considérant comme un
seul et même ennemi.
Ce sont des morts vivants, et la puissance du Glaive de Sommer vous
permet de multiplier par deux tous les points d'ENDURANCE qu'ils
perdront au cours du combat. Ils sont cependant insensibles à la
Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("LES ZOMBIES", 13, 16)], psychic_immune=True, undead=True)
    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur. Rendez-vous au :"))
        st.page_link("tomes/tome2/page_258.py", label="258", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
