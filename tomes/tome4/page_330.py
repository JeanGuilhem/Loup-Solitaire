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

check_inventory(current_page_number=330, book=4)

fr_text = """
Aux premières lueurs de l'aube, vous vous préparez à pénétrer
dans la vallée. La grand-route est enveloppée de brume, et
bientôt la forêt de Ruanon s'épaissit de part et d'autre. Un
enchevêtrement d'arbres aux troncs gris, de toutes formes et de
toutes tailles borde les bas-côtés. Après avoir chevauché
quelques minutes, vous découvrez, au bord de la route, la
carcasse d'un chariot calciné. Derrière, un sentier s'enfonce dans
les collines en direction de l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner les débris du chariot, rendez-vous au :"))
    st.page_link("tomes/tome4/page_38.py", label="38", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas y prêter attention et poursuivre votre chemin le long de la grand-route, rendez-vous au :"))
    st.page_link("tomes/tome4/page_175.py", label="175", icon="📄")

    st.write_stream(stream_text("Enfin, s'il vous semble plus opportun d'explorer le sentier qui monte dans les collines, rendez-vous au :"))
    st.page_link("tomes/tome4/page_293.py", label="293", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
