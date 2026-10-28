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

check_inventory(current_page_number=43, book=3)

fr_text = """
Vous tirez le Glaive d'Or hors de son fourreau et, d'un geste, vous
tranchez les cordes qui vous retiennent. Votre pied est à présent
libéré et vous sautez du traîneau quelques secondes avant qu'il
ne disparaisse dans le gouffre. Fenor se précipite vers vous et
vous tire en arrière, loin du bord instable de la crevasse. Vous
avez perdu vos chiens Kanu, votre traîneau et vos provisions,
mais vous êtes en vie. Vous sautez tous deux par-dessus la
crevasse, Fenor et vous, puis vous rejoignez les autres. Bien que
vous ayez perdu votre équipement, les guides sont d'accord pour
continuer la mission, tout en sachant que les épreuves qui vous
attendent désormais seront encore plus pénibles qu'auparavant.
Au loin, vous apercevez un étroit passage, au bord de la
banquise, là où elle jouxte la plaine de Hrod. A la nuit tombée,
vous atteignez l'abri de ce défilé et vous y installez votre
campement. En faisant l'inventaire des provisions qui vous
restent, vous vous rendez compte qu'il vous faudra diminuer les
rations de moitié si vous voulez que toute l'expédition puisse
atteindre la forteresse d'Ikaya. Le maigre Repas qui vous tient
lieu de dîner vous fait perdre 1 point d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_325.py", label="325", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
