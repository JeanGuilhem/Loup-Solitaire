import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=291, book=6)

fr_text = """
Ils continuent à jouer comme s'ils n'avaient pas remarqué votre
présence. Finalement, un soldat aux joues mal rasées daigne vous
répondre. « Voyons voir ce que les dés vont décider », dit-il, le
visage éclairé par les lueurs rougeoyantes de la lanterne. Il
crache dans sa main et jette le dé en os contre le mur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    roll = hazard_roll(key="t6_291")
    if roll is not None:
        if roll <= 4:
            st.write_stream(stream_text("Si vous avez tiré un chiffre entre 0 et 4, rendez-vous au :"))
            st.page_link("tomes/tome6/page_177.py", label="177", icon="📄")
        else:
            st.write_stream(stream_text("Si le chiffre que vous avez tiré est compris entre 5 et 9, rendez-vous au :"))
            st.page_link("tomes/tome6/page_309.py", label="309", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
