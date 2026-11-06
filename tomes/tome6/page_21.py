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

check_inventory(current_page_number=21, book=6)

fr_text = """
Au bout d'un long couloir en marbre gris, vous vous retrouvez face
à la porte de la bibliothèque. Il n'y a plus aucune trace des
hommes vêtus de brun que vous aviez aperçus en entrant dans la
cour, et tout est maintenant calme et silencieux comme dans un
tombeau. La bibliothèque est déserte également. Des milliers de
livres tapissent entièrement les murs, mais vous remarquez une
petite porte de l'autre côté de la pièce - probablement une
seconde issue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez examiner certains livres, rendez-vous au :"))
    st.page_link("tomes/tome6/page_302.py", label="302", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller ouvrir l'autre porte, rendez-vous au :"))
    st.page_link("tomes/tome6/page_127.py", label="127", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
