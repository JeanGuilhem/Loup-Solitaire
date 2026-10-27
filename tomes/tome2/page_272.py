import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=272, book=2)

fr_text = """
Quelqu'un ou quelque chose s'approche de la porte de la cale, de l'autre
côté du panneau. Si vous essayez de vous hisser sur le pont délabré, vos
jambes seront exposées et vous serez vulnérable à toute attaque venant
du fond de la cale. Il n'y a cependant pas d'autre issue. Compte tenu de
la situation, la meilleure chose à faire est de dégainer le Glaive de
Sommer et de vous préparer à combattre la créature malfaisante et
redoutable dont vous percevez la présence.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_5.py", label="5", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
