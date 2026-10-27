import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=71, book=2)

fr_text = """
Vous claquez la porte derrière vous et vous poussez le verrou. La
boutique est sombre, mais vous parvenez cependant à distinguer un
escalier à votre droite, une trappe au milieu du plancher et une porte
dans le mur du fond. Soudain, vous entendez le fracas d'une hache qui
vient de briser un panneau de la porte d'entrée. On vous a vu entrer
dans la boutique et la populace est en train de défoncer la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez ouvrir la trappe et vous cacher dans la cave, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_11.py", label="11", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez quitter la boutique par la porte du fond, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_54.py", label="54", icon="📄")

    st.write_stream(stream_text("Enfin, si vous décidez plutôt de monter l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome2/page_235.py", label="235", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
