import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=7, book=2)

fr_text = """
DORIER s'écarte d'un bond de la table et tire son épée. Un instant plus
tard, son frère GANON vient à sa rescousse. Il vous faut les combattre
tous deux comme s'il s'agissait d'un seul adversaire.
Votre attaque soudaine vous donne un avantage en raison de l'effet de
surprise. Vous ajouterez de ce fait 2 points à votre total d'HABILETÉ,
mais seulement lors du premier assaut. Au cours des assauts suivants,
votre total d'HABILETÉ reviendra à son niveau antérieur.
L'entraînement que les deux hommes ont suivi pour devenir Chevaliers
leur a donné une force mentale qui les met à l'abri de la Puissance
Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DORIER GANON", 28, 30)], first_round_modifier=2, psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Vous sortez vainqueur de ce combat. Rendez-vous au :"))
        st.page_link("tomes/tome2/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
