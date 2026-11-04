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

check_inventory(current_page_number=220, book=5)

fr_text = """
Votre maîtrise Kaï de l'Orientation vous indique que le sentier
sinueux mène directement à l'Arboretum du Zakhan : sa
cathédrale de verdure. Derrière le petit portail se trouve une
chambre secrète située dans le Palais supérieur, mais votre sens
Kaï ne vous en dit pas plus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez suivre le sentier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_391.py", label="391", icon="📄")

    st.write_stream(stream_text("Si vous préférez grimper les marches qui mènent au petit portail, rendez-vous au :"))
    st.page_link("tomes/tome5/page_352.py", label="352", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
