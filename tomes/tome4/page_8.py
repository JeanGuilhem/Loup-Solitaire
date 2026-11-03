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

check_inventory(current_page_number=8, book=4)

fr_text = """
Vos hommes amarrent le bateau à un anneau de fer rouillé puis
vous suivent dans l'escalier qui mène à l'arcade. Lorsque vous
arrivez sur un étroit palier, au sommet des marches de granit,
vous entendez d'étranges sons provenant de l'obscurité : on dirait
le sifflement d'un jet de vapeur. Le bruit dure quelques secondes,
puis il est interrompu brusquement par un claquement de fouet
et la voix d'un homme poussant des jurons.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans le tunnel qui s'ouvre devant vous, rendez-vous au :"))
    st.page_link("tomes/tome4/page_151.py", label="151", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas pénétrer dans ce souterrain, vous pouvez retourner sur le bateau et continuer le long de la rivière souterraine en vous rendant au :"))
    st.page_link("tomes/tome4/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
