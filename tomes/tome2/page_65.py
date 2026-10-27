import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=65, book=2)

fr_text = """
Tandis que vous courez le long de la rue de la Tour de Guet, vous
entendez derrière vous la voix du garde qui pousse des jurons. La voix
s'évanouit bientôt et vous arrivez sur la place du Tombeau. Devant
vous, dans la rue du même nom, quatre soldats marchent dans votre
direction. Vous les évitez en courant vers le sud pendant dix minutes
environ, le long d'une rue couverte de gros pavés. Enfin, vous
apercevez une grande écurie et un relais de diligence dont les contours
se dessinent dans l'obscurité, à quelque distance. Vous vous avancez
dans l'ombre et vous parvenez à grimper sur une échelle extérieure qui
mène dans un grenier à foin. Personne ne vous a vu et vous êtes en
sécurité pour la nuit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
