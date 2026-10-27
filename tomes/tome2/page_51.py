import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=51, book=2)

fr_text = """
Environ une heure plus tard, la diligence s'arrête devant le sanctuaire de
Kalanane. On dit que le sanctuaire a été édifié sur la tombe du roi Alin,
le premier souverain de Durenor et que, tout autour, pousse de l'herbe
de Laumspur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez cueillir un peu de cette herbe, rendez-vous au :"))
    st.page_link("tomes/tome2/page_103.py", label="103", icon="📄")

    st.write_stream(stream_text("Sinon, retournez dans la diligence en vous rendant au :"))
    st.page_link("tomes/tome2/page_249.py", label="249", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
