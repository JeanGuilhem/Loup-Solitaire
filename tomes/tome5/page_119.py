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

check_inventory(current_page_number=119, book=5)

fr_text = """
Les deux Gardes sont totalement pris au dépourvu par votre
attaque. La férocité et l'effet de surprise de celle-ci vous
permettent de ne pas déduire les points d'ENDURANCE que
vous pourriez perdre pendant les 3 premiers Assauts. Combattez
les deux Gardes comme s'il s'agissait d'un seul et même ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDES DU PALAIS", 16, 30)], ls_immune_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, cachez rapidement les deux corps avant de franchir l'entrée des jardins du Palais. Rendez-vous au :"))
        st.page_link("tomes/tome5/page_137.py", label="137", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
