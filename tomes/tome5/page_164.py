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

check_inventory(current_page_number=164, book=5)

fr_text = """
L'eau est de plus en plus épaisse et la puanteur qui se dégage des gaz délétères devient de plus en plus nauséabonde.
Brusquement, l'air est envahi par des milliers de mouches et
chaque fois que vous reprenez votre respiration, vous sentez au
fond de la gorge une bouillie épaisse d'insectes agglutinés. La
croûte noire et gluante qui recouvre vos yeux, vos narines et
votre bouche ainsi qu'un goût âcre et infect dans la gorge vous
soulèvent le cœur. Vous perdez 1 Point d'ENDURANCE. Comme
en réponse à vos prières, une échelle de fer se détache de
l'obscurité. Elle est fixée à la paroi du tunnel et monte jusqu'à
une plaque ronde en pierre encastrée dans le plafond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Si vous souhaitez grimper à l'échelle, rendez-vous au :"))
    st.page_link("tomes/tome5/page_31.py", label="31", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer à avancer dans le tunnel envahi par les insectes, rendez-vous au :'))
    st.page_link("tomes/tome5/page_139.py", label="139", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
