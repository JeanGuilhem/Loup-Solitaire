import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=38, book=2)

fr_text = """
Vous saisissez la hampe de la lance que vous enfoncez dans la cage
thoracique du Monstre d'Enfer. Celui-ci se met à hurler de douleur et de
rage en relâchant l'étreinte de ses doigts autour de votre cou. Vous
roulez alors sur vous-même pour échapper au Monstre hideux que vous
voyez se tordre sur le sol en essayant désespérément d'arracher la lance
de sa poitrine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez empoigner la lance pour l'enfoncer plus profondément dans le corps du Monstre d'Enfer, rendez-vous au :"))
    st.page_link("tomes/tome2/page_269.py", label="269", icon="📄")
    st.write_stream(stream_text("Si vous préférez prendre la fuite le plus vite possible, rendez-vous au :"))
    st.page_link("tomes/tome2/page_313.py", label="313", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
