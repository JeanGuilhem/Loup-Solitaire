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

check_inventory(current_page_number=156, book=4)

fr_text = """
Le tunnel aboutit bientôt au fond d'un puits de mine à la paroi
duquel est fixée une échelle qui mène à un autre tunnel situé à
une centaine de mètres au-dessus. L'entrée de ce tunnel se trouve
dans le mur ouest. Il n'y a pas d'autre issue au puits.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez monter l'échelle, rendez-vous au :"))
    st.page_link("tomes/tome4/page_212.py", label="212", icon="📄")

    st.write_stream(stream_text('Si vous préférez rebrousser chemin pour prendre le tunnel orienté au sud, rendez-vous au :'))
    st.page_link("tomes/tome4/page_101.py", label="101", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
