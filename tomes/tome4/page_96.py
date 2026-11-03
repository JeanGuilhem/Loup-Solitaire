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

check_inventory(current_page_number=96, book=4)

fr_text = """
Un tentacule fracasse le fond du bateau avec tant de force que
vous êtes projeté en l'air et que vous retombez tête la première
dans l'eau glacée de la rivière.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.write_stream(stream_text("Si vous tirez un chiffre entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome4/page_47.py", label="47", icon="📄")
    elif number is not None and number <= 8:
        st.write_stream(stream_text("Entre 5 et 8, rendez-vous au :"))
        st.page_link("tomes/tome4/page_234.py", label="234", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Enfin, si vous tirez le 9, rendez-vous au :"))
        st.page_link("tomes/tome4/page_334.py", label="334", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
