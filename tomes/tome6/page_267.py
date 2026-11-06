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

check_inventory(current_page_number=267, book=6)

fr_text = """
Vous chevauchez toute la nuit avec pour seul compagnon le vent qui
hurle dans la plaine de Varetta. La route, éclairée par un
brillant clair de lune, mène droit vers Soren. Au lever du jour,
vous arrivez à un petit hameau semblable aux autres, mais qui se
distingue néanmoins par la statue érigée devant la boutique du
maréchal-ferrant. C'est une haute statue en bronze représentant un
homme jeune au regard dur et menaçant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner la statue de plus près, rendez-vous au :"))
    st.page_link("tomes/tome6/page_220.py", label="220", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer votre route vers Soren, sans vous arrêter, rendez-vous au :"))
    st.page_link("tomes/tome6/page_73.py", label="73", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
