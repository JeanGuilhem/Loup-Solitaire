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

check_inventory(current_page_number=286, book=4)

fr_text = """
Vous attendez en retenant votre souffle. Bientôt, une rangée
d'hommes au visage hagard passe devant vous, encadrés par des
brigands qui frappent ceux qui hésitent ou s'écartent de la file.
Chacun de ces hommes reçoit l'ordre de pousser un chariot le
long du tunnel. Quelques instants plus tard, ils sont hors de vue.
Vous attendez encore, puis, lorsque vous estimez qu'il n'y a plus
de danger, vous reprenez votre chemin dans le tunnel en prenant
soin de vous dissimuler dans l'ombre. Enfin, vous arrivez au bout
du souterrain et vous émergez dans la lumière du jour. Un peu
plus loin sur votre gauche, vous apercevez une forêt touffue. La
voie ferrée mène à un portique dressé au-dessus d'un
entassement de minerai. C'est là que se trouvent à présent les
hommes et les Gardes que vous avez vus passer. Vous vous
précipitez en direction des arbres que vous parvenez à atteindre
sans avoir été repéré. Vous vous arrêtez un instant pour
reprendre votre souffle, puis vous poursuivez votre route dans la
forêt en direction de Ruanon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
