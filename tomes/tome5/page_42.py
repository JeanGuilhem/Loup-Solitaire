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

check_inventory(current_page_number=42, book=5)

fr_text = """
Votre maîtrise de la Discipline Kaï de l'Orientation vous indique
que l'allée est une impasse. Si vous cherchez à quitter la place par
là, vous êtes sûr de vous faire prendre ! Il ne vous reste plus que
deux possibilités : la haute porte hérissée de clous, sur votre
gauche, ou bien la rue pavée qui se trouve juste devant vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez passer par la porte, rendez-vous au :'))
    st.page_link("tomes/tome5/page_75.py", label="75", icon="📄")
    st.write_stream(stream_text('Si vous préférez prendre la rue pavée, rendez-vous au :'))
    st.page_link("tomes/tome5/page_169.py", label="169", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
