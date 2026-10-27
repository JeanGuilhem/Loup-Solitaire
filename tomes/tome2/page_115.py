import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=115, book=2)

fr_text = """
Devant la porte de la tour de guet, la végétation a été arrachée et le sol
bien tassé par de nombreux passages. Vous êtes en train de chercher un
trou de serrure sur cette porte à l'armature de fer lorsqu'elle s'ouvre
soudain. Un Chevalier de la Montagne Blanche se tient devant vous,
son épée levée face à son visage. « Exposez le but de votre visite et
parlez sans détour. Si vous mentez, je vous répondrai par le glaive. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez révéler au chevalier le véritable but de votre voyage à Durenor, rendez-vous au :"))
    st.page_link("tomes/tome2/page_80.py", label="80", icon="📄")
    st.write_stream(stream_text("Si vous voulez lui mentir, rendez-vous au :"))
    st.page_link("tomes/tome2/page_324.py", label="324", icon="📄")
    st.write_stream(stream_text("Si enfin vous préférez tirer votre épée et l'attaquer, rendez-vous au :"))
    st.page_link("tomes/tome2/page_162.py", label="162", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
