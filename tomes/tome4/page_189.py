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

check_inventory(current_page_number=189, book=4)

fr_text = """
Vous essayez à grands coups de rames d'amener ce qui reste du
bateau sur la rive opposée, mais, alors que vous plongez vos
avirons dans la rivière, ils vous sont arrachés des mains. Horrifié,
vous voyez l'un de vos patrouilleurs emporté dans l'eau noire par
un énorme tentacule gluant. Un instant plus tard, un autre
tentacule fracasse le fond du bateau avec une telle violence que
l'embarcation est projetée en l'air. Vous retombez tête la
première dans la rivière glacée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 4:
        st.write_stream(stream_text('Si vous tirez un chiffre de 0 à 4, rendez-vous au :'))
        st.page_link("tomes/tome4/page_234.py", label="234", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text('De 5 à 9, rendez-vous au :'))
        st.page_link("tomes/tome4/page_47.py", label="47", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
