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

check_inventory(current_page_number=280, book=7)

fr_text = """
Tavig est à peine visible à l'intérieur de l'énorme poing qui est en
train de se retirer dans le tunnel. Vous dégainez votre arme et
vous vous précipitez vers lui tandis que les grognements rauques
du monstre résonnent à vos oreilles. Vous devez frapper
immédiatement si vous voulez desserrer la prise du monstre et
sauver Tavig d'une mort affreuse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("POING GÉANT", 20, 42)], max_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous réduisez le total d'ENDURANCE de l'ennemi à zéro en 3 Assauts ou moins, rendez-vous au :"))
        st.page_link("tomes/tome7/page_291.py", label="291", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("Si le combat dure 4 Assauts ou plus, rendez-vous au :"))
        st.page_link("tomes/tome7/page_156.py", label="156", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
