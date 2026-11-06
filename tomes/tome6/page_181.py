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

check_inventory(current_page_number=181, book=6)

fr_text = """
Vous apprenez que l'homme s'appelle Barbenoire et qu'il est
originaire de Soren, une ville située à l'ouest de Varetta. Il est
sergent d'armes et sert sous les ordres d'un capitaine de
mercenaires. Sa compagnie revient d'une campagne contre les
Magadoniens. Il veut maintenant vous présenter à son capitaine
qui, dit-il, est le meilleur soldat qu'il ait eu l'honneur de servir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez accepter son offre, rendez-vous au :"))
    st.page_link("tomes/tome6/page_256.py", label="256", icon="📄")

    st.write_stream(stream_text("Si vous préférez décliner son offre et continuer votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
