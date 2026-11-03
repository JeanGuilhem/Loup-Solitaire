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

check_inventory(current_page_number=56, book=4)

fr_text = """
Vous frappez le Garde, lui infligeant une profonde blessure au
cou. Il pousse un hurlement et se tourne pour vous faire face, un
sabre à la main.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE BLESSÉ", 12, 18)], max_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous gagnez le combat en 3 Assauts ou moins, rendez-vous au :"))
        st.page_link("tomes/tome4/page_69.py", label="69", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("S'il vous faut plus de 3 Assauts pour l'emporter, rendez-vous au :"))
        st.page_link("tomes/tome4/page_203.py", label="203", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
