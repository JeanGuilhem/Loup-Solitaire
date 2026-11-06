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

check_inventory(current_page_number=227, book=6)

fr_text = """
Les cavaliers ont à peine parcouru quelques mètres que le
dernier soldat de la colonne se retourne pour surveiller Cyrilus
qui commence à glisser de sa selle. Vous sautez aussitôt dans les
taillis qui bordent la route, mais le soldat vous aperçoit et crie à
ses camarades : « Il est là, derrière ! » Quelques secondes plus
tard, vous entendez les martèlements de leurs sabots. Les
cavaliers ont fait demi-tour et se rapprochent de votre cachette.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Arc, vous pouvez leur tirer dessus au moment où ils passeront devant vous. Rendez-vous au :"))
    if can_shoot():
        st.page_link("tomes/tome6/page_20.py", label="20", icon="📄")
    else:
        st.write("*Il vous faut un Arc, un Carquois et une flèche.*")
        st.page_link("tomes/tome6/page_20.py", label="20", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous préférez vous préparer à les combattre par d'autres moyens, rendez-vous au :"))
    st.page_link("tomes/tome6/page_203.py", label="203", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
