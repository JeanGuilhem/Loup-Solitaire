import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=310, book=6)

fr_text = """
Vous avez taillé le monstre en pièces, mais tous ses membres
sanguinolents éparpillés dans la crypte bougent toujours, et
rampent vers vous dans un mouvement mécanique et aveugle.
Vous sentez tout à coup une patte à moitié déchiquetée grimper
sur votre jambe en enfonçant ses griffes dans votre chair. (Vous
perdez 2 points d'ENDURANCE.) Tandis que vous luttez pour
dégager la patte, les membres mutilés du Dakomyd commencent
à se regrouper pour une nouvelle attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous souhaitez attaquer la créature avant qu'elle soit complètement reformée, rendez-vous au :"))
    st.page_link("tomes/tome6/page_323.py", label="323", icon="📄")

    st.write_stream(stream_text('Si vous préférez ouvrir la tombe pour prendre la Pierre de la Sagesse, rendez-vous au :'))
    st.page_link("tomes/tome6/page_293.py", label="293", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
