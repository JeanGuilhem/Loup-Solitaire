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

check_inventory(current_page_number=387, book=5)

fr_text = """
Votre cœur défaille. Il n'y a pas d'autres marches qui descendent
de la plate-forme et vous voilà pris au piège ! Avant que vous ne
pensiez à un moyen de vous en sortir, les Drakkars surgissent de
l'arche et attaquent :
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DRAKKARS", 17, 35)])
    if outcome is None:
        # sauter de la tour reste possible à tout moment du combat
        st.write_stream(stream_text("La seule façon d'échapper au combat est de vous laisser tomber de la tour vers les jardins, à quelque 30 mètres en contrebas. Si vous voulez sauter, rendez-vous au :"))
        st.page_link("tomes/tome5/page_205.py", label="205", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous gagnez le combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_341.py", label="341", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
