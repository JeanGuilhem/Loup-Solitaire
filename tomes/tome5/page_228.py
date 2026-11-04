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

check_inventory(current_page_number=228, book=5)

fr_text = """
Vous courez tête baissée à travers un enchevêtrement d'arbres et
de racines et vous parvenez à semer vos impitoyables ennemis.
Vous arrivez à une petite tonnelle en bois, de forme arrondie, à
moitié dissimulée par un rideau de plantes grimpantes. Scrutant
le feuillage épais, vous remarquez que les plantes montent
jusqu'à un balcon en fer forgé qui mène droit à un portail en
pierre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous hisser sur le balcon en vous accrochant au lierre, et vous enfuir ensuite par la porte en pierre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_352.py", label="352", icon="📄")

    st.write_stream(stream_text("Si vous préférez essayer de sortir de l'Arboretum en trouvant une issue au niveau du sol, rendez-vous au :"))
    st.page_link("tomes/tome5/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
