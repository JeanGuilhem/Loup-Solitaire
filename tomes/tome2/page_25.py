import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=25, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous parcourez du regard la taverne où s'entasse une foule de buveurs,
et vous remarquez que de nombreux villageois jouent à des jeux de
hasard. Près de l'entrée principale, un jeune personnage à l'allure louche
est assis devant une table sur laquelle trois tasses d'argile sont
retournées. Il les change sans cesse de place en mettant au défi qui veut
l'entendre de deviner sous laquelle de ces trois tasses est cachée une
bille de verre. Il promet de donner au gagnant le double de la somme
que ce dernier aura misée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez les Disciplines Kaï du Sixième Sens ou de la Maîtrise Psychique de la Matière, rendez-vous au :"))
    if has_kai("Le Sixième Sens") or has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome2/page_116.py", label="116", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_116.py", label="116", icon="📄", disabled=True)
    st.write_stream(stream_text("Si ces deux Disciplines vous sont étrangères, rendez-vous au :"))
    st.page_link("tomes/tome2/page_153.py", label="153", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
