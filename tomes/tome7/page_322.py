import streamlit as st
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

check_inventory(current_page_number=322, book=7)

fr_text = """
Vous avancez le long du passage pendant plusieurs minutes
avant d'arriver à un brusque tournant sur la gauche.
Prudemment, vous regardez de l'autre côté, averti par vos
instincts Kaï d'une éventuelle menace. Vous apercevez un rayon
de lumière qui brille en travers du couloir. Ce tunnel a l'air
semblable à tous les autres tunnels du labyrinthe, mais vous êtes
cependant certain qu'il recèle un piège mortel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez enjamber le rayon de lumière et continuer le long du passage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_88.py", label="88", icon="📄")
    st.write_stream(stream_text("Si vous choisissez de passer à travers le rayon, rendez-vous au :"))
    st.page_link("tomes/tome7/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
