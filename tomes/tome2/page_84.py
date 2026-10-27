import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=84, book=2)

fr_text = """
Dans l'entrée principale, un vieil homme est assis ; il arbore une longue
barbe et semble fort aimable. Penché sur un lutrin, il est en train
d'étudier un énorme livre à la reliure de cuir. Sa lecture l'absorbe tant
qu'il n'a pas remarqué votre présence dans l'enceinte de l'hôtel de ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez lui demander le chemin du consulat du Sommerlund, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_211.py", label="211", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez repartir et trouver vous-même votre chemin, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
