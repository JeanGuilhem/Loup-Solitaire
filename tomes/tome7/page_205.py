import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=205, book=7)

fr_text = """
Vous sentez que cet homme est paralysé par la peur. En effet,
une aura de malfaisance irradie depuis l'entrée du tunnel et se
propage comme une vague de chaleur diabolique. Ses radiations
deviennent bientôt si intenses que vous ne pouvez plus utiliser
votre discipline, et vous ne parvenez même pas à savoir si le
guerrier est un ami ou un ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez tirer une arme pour vous défendre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_95.py", label="95", icon="📄")

    st.write_stream(stream_text("Si vous voulez éviter toute confrontation en courant vers l'entrée de l'autre tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_47.py", label="47", icon="📄")

    st.write_stream(stream_text("Si vous possédez un arc et que vous souhaitez tirer sur le guerrier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_79.py", label="79", icon="📄", disabled=not can_shoot())

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
