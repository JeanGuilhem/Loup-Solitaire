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

check_inventory(current_page_number=260, book=6)

fr_text = """
« Nous n'avons besoin de personne, ricane un guerrier au visage
rougeaud marqué de la maladie. Mêlez-vous de ce qui vous regarde
ou vous aurez affaire à nos épées. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez vous présenter, rendez-vous au :"))
    st.page_link("tomes/tome6/page_130.py", label="130", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez les prendre au mot et les défier au combat, rendez-vous au :"))
    st.page_link("tomes/tome6/page_159.py", label="159", icon="📄")

    st.write_stream(stream_text("Si vous préférez les ignorer, vous installer à une table isolée et commander un repas, rendez-vous au :"))
    st.page_link("tomes/tome6/page_172.py", label="172", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
