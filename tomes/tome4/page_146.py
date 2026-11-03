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

check_inventory(current_page_number=146, book=4)

fr_text = """
Le brigand tombe dans l'eau et son cadavre disparaît. Vous
sautez d'une pierre à l'autre à la poursuite des deux Pillards qui
ont survécu à l'embuscade et qui essaient à présent de rejoindre
la rive opposée pour donner l'alerte à leurs camarades, restés
dans le chariot. Les brigands surgissent bientôt du véhicule et
vous constatez alors avec horreur qu'ils sont tous armés d'arcs.
Ils les tendent aussitôt en visant vos patrouilleurs. Vous hurlez
pour avertir vos hommes, mais à cet instant une flèche à la
pointe d'acier vous effleure le sommet du crâne en vous
précipitant dans les eaux sombres et bouillonnantes de la rivière
Xane.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
