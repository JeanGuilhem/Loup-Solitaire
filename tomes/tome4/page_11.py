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

check_inventory(current_page_number=11, book=4)

fr_text = """
Vous avez parcouru une vingtaine de mètres environ lorsque
vous arrivez soudain devant une paroi rocheuse. Vous vous
trouvez dans un cul-de-sac. Ce tunnel a été creusé récemment et
vous ne pouvez pas aller plus loin dans cette direction. Il ne vous
reste donc plus qu'à retourner au croisement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez un chiffre entre 0 et 4, rendez-vous au 97. Entre 5 et 9, rendez-vous au 190."))
    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome4/page_97.py", label="97", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome4/page_190.py", label="190", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
