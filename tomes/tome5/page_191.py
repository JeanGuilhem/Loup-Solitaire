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

check_inventory(current_page_number=191, book=5)

fr_text = """
Vous réussissez à grimper lentement sur les avirons et, une fois
parvenu au bastingage, des mains vous saisissent fermement par
le col de votre manteau et vous hissent par-dessus bord. «Livrez-
moi Loup Solitaire, hurle Maouk depuis le quai. C'est un ordre
du Zakhan ! » Les membres de l'équipage se dévisagent, déçus et
peinés. Ils savent que les menaces de Maouk ne sont pas de
vaines paroles et vous ne pouvez pas exiger de ces hommes qu'ils
sacrifient leur vie et celle de leur famille pour vous sauver. Vous
devez adopter une nouvelle tactique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous décidez de vous rendre à Maouk, rendez-vous au :'))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    st.write_stream(stream_text('Si vous préférez plonger par-dessus bord pour échapper à Maouk, rendez-vous au :'))
    st.page_link("tomes/tome5/page_142.py", label="142", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
