import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=67, book=2)

fr_text = """
Vous arrivez très vite à la conclusion que l'imposteur a dû s'enfuir par
l'entrée principale de la taverne ; s'il est resté dans les environs, il doit
probablement se trouver sur la place principale ou à proximité. Vous
fouillez les ruelles et les maisons autour de la place, mais vous ne
découvrez pas la moindre trace du fuyard. Plutôt que de perdre votre
temps en vaines recherches, vous décidez alors de revenir sur le quai.
Là, vous détachez l'amarre d'un canot et vous ramez en direction du
Sceptre Vert en éprouvant un sentiment de malaise : vous ne vous
attendiez pas à ce que vos ennemis se manifestent si tôt, dès les
premières heures de votre mission.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_300.py", label="300", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
