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
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=121, book=3)

fr_text = """
Vous êtes sur le point de perdre votre concentration lorsque
enfin la corde enroulée autour de votre pied se relâche et vous
libère. Vous sautez alors du traîneau une seconde à peine avant
qu'il ne tombe dans la crevasse et vous entendez les hurlements
terrifiants des chiens Kanu qui sont précipités dans l'obscurité
du gouffre. Fenor vient aussitôt vous secourir et vous tire en
arrière pour vous éloigner du bord instable dont la glace
commence à céder sous votre poids. Vous avez perdu vos chiens,
votre traîneau et la plus grande partie de vos provisions, mais au
moins vous êtes vivant. Fenor et vous-même sautez d'un bond
par-dessus la crevasse et vous rejoignez les autres. Après une
longue discussion, vos guides acceptent de poursuivre la mission,
bien que les épreuves qui vous attendent promettent d'être deux
fois plus pénibles en raison de la perte de votre équipement. Au
loin, vous apercevez un passage étroit qui marque la jonction
entre la banquise et la plaine de Hrod. A la nuit tombée, vous
avez atteint l'abri de ce défilé et vous y installez votre
campement. En faisant l'inventaire des vivres qui vous restent,
vous vous apercevez qu'il faudra diviser les rations par deux si
vous voulez que l'expédition puisse atteindre Ikaya. Le maigre
Repas que vous prenez en guise de dîner vous fait perdre 1 point
d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_325.py", label="325", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
