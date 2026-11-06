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

check_inventory(current_page_number=222, book=6)

fr_text = """
Le monstre plonge sur vous du haut des escaliers. Vous restez
immobile puis vous recevez la créature d'un coup bien ajusté qui
lui ouvre une blessure béante dans le cou, la tuant
instantanément. Mais la force de votre coup n'est pas assez
puissante pour faire basculer la lourde masse du monstre sur le
côté, et il vous écrase sous lui contre les dalles. Vous perdez 12
points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-12)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-12)

    st.write_stream(stream_text("Si vous êtes toujours vivant, rendez-vous au :"))
    st.page_link("tomes/tome6/page_106.py", label="106", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
