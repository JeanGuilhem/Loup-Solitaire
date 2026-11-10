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

check_inventory(current_page_number=287, book=7)

fr_text = """
Rassemblant toutes vos forces, vous courez le long du tunnel,
aiguillonné par l'effrayant grincement des crocs de la créature. Le
passage se termine quelques mètres plus loin, mais un autre part
sur la droite. Vous tournez au coin, le plus vite possible, en vous
cognant douloureusement l'épaule contre le mur et vous
continuez à courir, mais vous êtes bientôt obligé de vous arrêter
car le tunnel est obstrué. Un amas d'immenses bulles brillantes
flotte devant vous dans l'obscurité, entre les brumes du plafond
et le sol lisse. Une brise légère les pousse en avant et les fait
rebondir dans votre direction tandis que vous entendez à
nouveau les hurlements du loup derrière vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez avancer à travers les bulles pour continuer le long du tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_84.py", label="84", icon="📄")

    st.write_stream(stream_text("Si vous voulez rester sur place pour vous battre avec le loup, rendez-vous au :"))
    st.page_link("tomes/tome7/page_245.py", label="245", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous tailler un chemin à travers les bulles à l'aide de votre épée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_218.py", label="218", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
