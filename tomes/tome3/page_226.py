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

check_inventory(current_page_number=226, book=3)

fr_text = """
Vous agitez frénétiquement le pied et vous parvenez à vous
libérer au moment précis où le traîneau bascule dans la crevasse.
Fenor se précipite alors vers vous et vous tire en arrière pour
vous éloigner du bord instable. Ensuite, vous sautez tous deux
par-dessus l'ouverture béante que vous franchissez sans
encombre, et vous rejoignez les autres. Vous avez perdu votre
traîneau, vos chiens et la plus grande partie de vos vivres, mais
vous êtes vivant. Bien que cette perte doive inévitablement
entraîner des épreuves supplémentaires dans la suite de votre
voyage, vos guides acceptent de poursuivre la mission. Au loin,
vous apercevez un étroit défilé, à la jonction de la banquise et de
la plaine de Hrod. A la nuit tombée, vous atteignez l'abri de ce
défilé et vous décidez d'y établir votre campement. En faisant
alors l'inventaire des vivres qui vous restent, vous vous apercevez
qu'il faudra diminuer les rations de moitié d'ici à Ikaya. Dans
l'immédiat, le maigre Repas qui vous tient lieu de dîner vous fait
perdre 1 point d'ENDURANCE.
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
