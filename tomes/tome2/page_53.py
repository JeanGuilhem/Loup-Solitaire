import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=53, book=2)

fr_text = """
Vous entendez des murmures parmi l'équipage ; de temps à autre, vous
percevez distinctement certains mots : les hommes parlent de «
vaisseaux fantômes » et de « malédiction » mais les murmures cessent
lorsque le capitaine appelle tout le monde sur le pont. Le silence alors
s'installe à bord du Sceptre Vert tandis que le capitaine Kelman
s'adresse à l'équipage d'une voix puissante : « Nous sommes à trois
jours de mer de Port Bax, dit-il, mais avec un bon vent et du cœur au
ventre, nous pourrons y jeter l'ancre et festoyer à terre dans moins de
deux jours. Le feu a détruit la plupart de nos vivres et nous devrons par
conséquent nous contenter d'un repas par jour. Un garde sera mis en
faction devant le baril d'eau douce. Nous sommes forts cependant et
nous supporterons l'épreuve mais sachez que quiconque sera surpris à
voler recevra cent coups de fouet. C'est tout ce que j'avais à dire ».
L'équipage ne semble pas très satisfait des décisions du capitaine, mais
personne n'ose défier son autorité. Plus tard dans l'après-midi,
l'équipage et le capitaine vous invitent chacun de son côté à prendre
votre repas du soir en leur compagnie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez dîner avec le capitaine, rendez-vous au :"))
    st.page_link("tomes/tome2/page_321.py", label="321", icon="📄")

    st.write_stream(stream_text("Si vous préférez manger avec l'équipage, rendez-vous au :"))
    st.page_link("tomes/tome2/page_154.py", label="154", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
