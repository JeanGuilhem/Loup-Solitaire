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

check_inventory(current_page_number=146, book=6)

fr_text = """
A midi, les collines sont déjà loin derrière vous, et vous
découvrez maintenant les cimes enneigées des monts Ceners. Amory
se trouve au sud, tapie au pied du massif montagneux. La fatigue
de la route commence à se faire sentir, mais vous savez qu'il
vous faut presser le pas afin d'atteindre la ville avant la
tombée de la nuit. Vous arrivez bientôt à un croisement où un
poteau en pierre indique deux directions.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez continuer la route vers Amory, rendez-vous au :"))
    st.page_link("tomes/tome6/page_96.py", label="96", icon="📄")

    st.write_stream(stream_text("Si vous préférez changer votre itinéraire et tourner vers Soren, rendez-vous au :"))
    st.page_link("tomes/tome6/page_247.py", label="247", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
