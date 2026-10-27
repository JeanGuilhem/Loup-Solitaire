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

check_inventory(current_page_number=218, book=2)

fr_text = """
Le capitaine Zombie est mort, mais vous vous trouvez encerclé par les
visages macabres des membres de l'équipage ; ils sont au nombre de
vingt, armés de coutelas et de haches.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez les combattre, rendez-vous au :'))
    st.page_link("tomes/tome2/page_43.py", label="43", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous enfuir en saisissant une corde qui pend à proximité et en l'utilisant pour vous élancer sur le pont d'un navire de Durenor, rendez-vous au :"))
    st.page_link("tomes/tome2/page_105.py", label="105", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
