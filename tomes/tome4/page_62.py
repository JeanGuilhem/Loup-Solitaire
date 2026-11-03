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

check_inventory(current_page_number=62, book=4)

fr_text = """
Le brigand se lève d'un bond et vous attaque avec sa masse
d'armes. Vous êtes toujours à terre et vous devrez, de ce fait,
réduire de deux points votre total d'HABILETÉ au cours des trois
premiers Assauts. A partir du quatrième Assaut, vous pouvez
vous relever et retrouver votre total normal d'HABILETÉ. Il vous
est impossible de prendre la fuite et il vous faut combattre ce
Guerrier Pillard jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # à terre pendant les 3 premiers assauts : -2 HABILETÉ
    outcome = combat([("GUERRIER PILLARD", 17, 24)], first_round_modifier=-2, first_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome4/page_148.py", label="148", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
