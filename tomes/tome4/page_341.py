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

check_inventory(current_page_number=341, book=4)

fr_text = """
Un cercle de visages qui n'ont pas été rasés depuis plusieurs
jours vous entoure. Un soldat vous soulève doucement la jambe,
tandis qu'un autre arrache la flèche enfoncée dans votre cuisse.
Son geste a été si rapide que vous n'avez pas même eu le temps
de pousser un cri de douleur. « Vous avez eu de la chance,
Seigneur Kaï, dit le soldat en appliquant des herbes de Laumspur
sur votre membre blessé. La blessure est propre et elle n'a pas
beaucoup saigné. » Vous perdez 4 points d'ENDURANCE, mais
l'action rapide de cet homme vous a évité d'avoir la jambe
infectée. Les soldats vous portent ensuite, le capitaine Gayal et
vous-même, dans la tour de guet.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_116.py", label="116", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
