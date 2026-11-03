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

check_inventory(current_page_number=111, book=4)

fr_text = """
Vous vous mettez en position et vous vous concentrez pour
choisir le meilleur moment où frapper. Tous vos sens de Guerrier
Kaï en éveil, vous lancez une attaque éclair. Plongeant sous le
cimeterre qui siffle au-dessus de votre tête, vous tranchez la
sangle de selle de votre adversaire. La selle bascule sur le côté et
le cavalier tombe à bas de son cheval, s'écrasant à terre dans un
nuage de poussière et de cendre. Vous avancez vers lui pour
l'achever, mais il est prompt à réagir et se relève d'un bond. Il
vous fait face à présent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez le combattre, rendez-vous au :'))
    st.page_link("tomes/tome4/page_90.py", label="90", icon="📄")

    st.write_stream(stream_text('Si vous préférez prendre la fuite, rendez-vous au :'))
    st.page_link("tomes/tome4/page_163.py", label="163", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
