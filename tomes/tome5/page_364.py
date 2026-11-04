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

check_inventory(current_page_number=364, book=5)

fr_text = """
La pièce commence à bouger, tout d'abord presque imperceptiblement, mais en l'espace de quelques secondes, les
murs de la cabine et les Nains dansent sous vos yeux dans un
brouillard de couleurs. Vous vous accrochez au rebord de la table
pour essayer de surmonter cette atroce sensation de vertige et
vous serrez la table jusqu'à ce que vos articulations deviennent
complètement blanches. Tous les sons vous semblent lointains,
comme s'ils vous parvenaient des profondeurs d'une cave.
Soudain, la tête ne vous tourne plus, mais les ténèbres vous
envahissent : vous venez de vous évanouir et vous gisez sur le sol,
inconscient.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_380.py", label="380", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
