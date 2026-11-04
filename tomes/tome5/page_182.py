import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=182, book=5)

fr_text = """
Vous arrivez dans une pièce au haut plafond voûté. Dans le mur
sud, il y a une grande porte renforcée par de gros clous près de
laquelle se trouve un râtelier où sont suspendus un Javelot et une
Épée. Si vous le désirez, vous pouvez prendre l'une de ces armes
(ou bien les deux). Au nord, sous un porche en forme de fer à
cheval, joliment décoré, un autre passage conduit hors de la
pièce.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("LANCE", key="javelot", label="Prendre le Javelot (Lance)")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    st.write_stream(stream_text('Si vous souhaitez suivre ce passage, rendez-vous au :'))
    st.page_link("tomes/tome5/page_132.py", label="132", icon="📄")

    st.write_stream(stream_text('Si vous préférez écouter à la porte, rendez-vous au :'))
    st.page_link("tomes/tome5/page_115.py", label="115", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
