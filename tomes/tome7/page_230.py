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

check_inventory(current_page_number=230, book=7)

fr_text = """
Aussitôt après avoir avalé les pilules, vos poumons cessent de
vous faire mal et tout votre corps se détend. Les pores de votre
peau absorbent l'oxygène de l'eau, et vous échappez ainsi à la
noyade. Vous pouvez dès à présent chercher un moyen pour
sortir de cette tombe remplie d'eau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer d'ouvrir la porte verrouillée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_66.py", label="66", icon="📄")

    st.write_stream(stream_text("Si vous préférez examiner la statue, rendez-vous au :"))
    st.page_link("tomes/tome7/page_168.py", label="168", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
