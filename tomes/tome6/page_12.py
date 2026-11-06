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

check_inventory(current_page_number=12, book=6)

fr_text = """
La flèche va se planter dans la patte gauche de la créature qui
perd aussitôt l'équilibre en poussant un hurlement déchirant. La
rapidité de votre attaque vous laisse à présent le temps de
dégainer une arme à main afin d'affronter à nouveau l'ignoble
monstre. La créature s'est effondrée, face contre terre. Grâce à
la position délicate dans laquelle se trouve votre adversaire,
vous ne perdez aucun point d'ENDURANCE durant les deux premiers
Assauts du combat, quoi qu'il arrive. Par ailleurs, vous pouvez
abandonner la lutte à tout moment en vous échappant par le porche
d'entrée de la chapelle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("YAMSARK", 22, 32)], ls_immune_rounds=2, flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Si vous souhaitez prendre la fuite, rendez-vous au :"))
        st.page_link("tomes/tome6/page_305.py", label="305", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome6/page_112.py", label="112", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
