import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=146, book=2)

fr_text = """
Vous aviez raison. Ce nuage est formé par une nuée d'énormes
Bêtalzans et de Kraans, une espèce plus petite, mais tout aussi mortelle.
Pendant sous leur ventre noir, ils tiennent dans leurs serres d'immenses
filets dans lesquels s'entassent des GLOKS. Les Bêtalzans fondent alors
sur le Sceptre Vert et un filet rempli de Gloks hurlants s'écrase sur le
pont. Certains n'ont pas survécu à la chute mais la plupart sont
indemnes et vous attaquent sans tarder. Il vous faut les combattre en les
considérant comme un seul et même ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GLOKS", 15, 15)])
    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome2/page_345.py", label="345", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
