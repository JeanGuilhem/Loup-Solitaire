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

check_inventory(current_page_number=204, book=7)

fr_text = """
La température augmente à chacun de vos pas mais, lorsque vous
atteignez les premières flammes, vous ne sentez ni chaleur ni
douleur. Les flammes sont rafraîchissantes comme une douce
brise d'été ! Vous traversez rapidement les jets de flamme
inoffensifs et vous continuez à avancer le long du passage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
