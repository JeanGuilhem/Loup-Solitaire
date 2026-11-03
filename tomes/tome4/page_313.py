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

check_inventory(current_page_number=313, book=4)

fr_text = """
Vous posez les mains sur le bras du patrouilleur blessé en vous
efforçant de remettre en place ses os fracassés. Vous le pansez
ensuite à l'aide de lambeaux d'étoffe arrachés à sa tunique.
Pendant ce temps, l'autre patrouilleur a réussi à se libérer et à
trancher deux autres tentacules gluants accrochés à la coque
brisée du bateau. Il saisit maintenant les avirons et rame
frénétiquement en direction de la rive opposée. A peine,
cependant, a-t-il plongé les rames dans l'eau qu'un craquement
terrifiant retentit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_96.py", label="96", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
