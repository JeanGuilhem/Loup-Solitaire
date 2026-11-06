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

check_inventory(current_page_number=303, book=6)

fr_text = """
Votre flèche atteint la cible avec une extrême précision et pénètre
dans l'armure du cavalier à la base du crâne. Il lève les bras,
vacille sur sa selle puis s'écrase au milieu du pont dans un bruit
métallique. Si votre flèche ne l'a pas tué, il a sûrement trouvé la
mort dans sa chute, étant donné le poids de son armure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez vous arrêter pour fouiller le corps, rendez-vous au :'))
    st.page_link("tomes/tome6/page_139.py", label="139", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous lancer à la poursuite des ravisseurs sans plus attendre, rendez-vous au :'))
    st.page_link("tomes/tome6/page_39.py", label="39", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
