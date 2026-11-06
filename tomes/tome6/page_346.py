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

check_inventory(current_page_number=346, book=6)

fr_text = """
Assis à une table près du feu, vous apercevez trois soldats au
visage fatigué, couverts de poussière et de saleté. Ils portent sur
la poitrine un insigne avec deux épées croisées, emblème de
Varetta. Vous comprenez qu'il s'agit de soldats de fortune,
probablement des mercenaires à la solde du Capitaine, qui est lui
aussi de cette ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez vous joindre à eux pour essayer d'en apprendre un peu plus sur Varetta, rendez-vous au :"))
    st.page_link("tomes/tome6/page_125.py", label="125", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous diriger vers le bar et demander une chambre pour la nuit, rendez-vous au :'))
    st.page_link("tomes/tome6/page_232.py", label="232", icon="📄")

    st.write_stream(stream_text('Enfin, si vous voulez vous attabler seul et commander à dîner, rendez-vous au :'))
    st.page_link("tomes/tome6/page_172.py", label="172", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
