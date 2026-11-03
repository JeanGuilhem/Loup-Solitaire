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

check_inventory(current_page_number=210, book=4)

fr_text = """
Cette ville vous inspire un sentiment de malaise. Jusqu'à présent,
vous n'avez vu marcher dans la rue que des femmes et des
enfants traînant les pieds. A aucun moment la silhouette d'un
homme n'est apparue. Les habitants semblent nerveux et évitent
votre regard. Votre instinct de Guerrier Kaï vous incite à quitter
les lieux le plus vite possible.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez obéir à cet instinct, rendez-vous au :'))
    st.page_link("tomes/tome4/page_67.py", label="67", icon="📄")

    st.write_stream(stream_text('Si vous préférez ne pas en tenir compte, vous pouvez entrer dans la taverne en vous rendant au :'))
    st.page_link("tomes/tome4/page_132.py", label="132", icon="📄")

    st.write_stream(stream_text('Enfin il vous est également possible de poursuivre votre chemin le long de la rue. Rendez-vous pour cela au :'))
    st.page_link("tomes/tome4/page_301.py", label="301", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
