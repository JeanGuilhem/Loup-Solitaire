import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=313, book=2)

fr_text = """
Les cris terrifiants des Monstres d'Enfer s'évanouissent enfin derrière
vous et vous pouvez vous arrêter quelques instants pour reprendre votre
souffle. Vous grimacez alors de douleur, car les doigts de
l'épouvantable créature vous ont brûlé la gorge, vous infligeant des
blessures cuisantes qui vous coûtent 4 points d'ENDURANCE. Vous
déchirez un pan de votre tunique pour en faire un bandage, puis vous
poursuivez votre route le long du tunnel de Tarnalin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_349.py", label="349", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
