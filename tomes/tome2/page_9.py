import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=9, book=2)

fr_text = """
Vous êtes arrivé au quatorzième jour de votre quête. L'aube vient de se
lever lorsque vous ouvrez les yeux ; vous contemplez alors un spectacle
à vous couper le souffle : Hammardal, la cité des montagnes, se dresse
devant vous. Contrairement aux autres villes des Fins de Terre, la
capitale du royaume de Durenor n'a jamais eu besoin qu'on lui élève de
fortifications. Les sommets montagneux qui l'entourent offrent une bien
meilleure protection à ses habitants. Le carrosse qui vous emporte file
parmi les riches terres des fermes environnantes en direction de la cité
aux hautes tours et aux larges avenues. Au centre même d'Hammardal,
la Tour du Roi s'élève sur une colline. C'est un magnifique édifice de
pierre et de verre devant les portes duquel s'arrête votre attelage. Pour
la première fois, vous prenez alors conscience que le privilège d'avoir
brandi le Glaive de Sommer vous fera désormais entrer dans les plus
anciennes légendes des Fins de Terre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_196.py", label="196", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
