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

check_inventory(current_page_number=361, book=5)

fr_text = """
Vous plongez sous la grand-voile puis vous grimpez sur la plate-forme au moment où se déroule une lutte désespérée. Le
magicien aux cheveux blonds est en effet cloué sur le pont par
une lance qui lui a transpercé le bras gauche. De sa main droite
armée d'un bâton, il tente de repousser son agresseur, mais
celui-ci, un Drakkar, s'aperçoit de votre présence. Il se retourne
brusquement et tire de son fourreau un cimeterre noir à lame recourbée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DRAKKAR", 18, 25)], max_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat en 3 Assauts, ou moins, rendez-vous au :"))
        st.page_link("tomes/tome5/page_288.py", label="288", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("Si la bataille se poursuit jusqu'à un 4e Assaut, cessez le combat et rendez-vous immédiatement au :"))
        st.page_link("tomes/tome5/page_382.py", label="382", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
