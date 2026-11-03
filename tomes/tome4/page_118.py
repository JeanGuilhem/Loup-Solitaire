import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=118, book=4)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
La porte de fer est fermée à clé. Elle comporte une grosse
poignée à laquelle est suspendu un Fouet. Si vous voulez prendre
ce Fouet, inscrivez-le sur votre Feuille d'Aventure dans la case
des objets contenus dans votre Sac à Dos.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("FOUET", key="fouet", label="Prendre le Fouet")

    st.write_stream(stream_text('Si vous possédez une Clé de Fer, vous pouvez ouvrir la porte en vous rendant au :'))
    if has_item("CLÉ DE FER"):
        st.page_link("tomes/tome4/page_308.py", label="308", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_308.py", label="308", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne possédez pas cette Clé, ou si vous ne souhaitez pas ouvrir la porte, vous pouvez quitter les lieux en empruntant un escalier en colimaçon. Pour monter cet escalier, rendez-vous au :'))
    st.page_link("tomes/tome4/page_170.py", label="170", icon="📄")

    st.write_stream(stream_text('Si vous préférez descendre les marches, rendez-vous au :'))
    st.page_link("tomes/tome4/page_228.py", label="228", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
