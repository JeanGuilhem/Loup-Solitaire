import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=325, book=2)

fr_text = """
Votre Sens de l'Orientation vous indique que le couloir de gauche est le
chemin le plus court pour Hammardal ; vous gagnerez environ 3
kilomètres en l'empruntant. Un peu avant la bifurcation, une grande
flaque d'eau s'est formée au milieu de la chaussée et les traces de pas de
deux hommes qui ont marché dans la flaque sont visibles sur le sol.
Chacun d'eux a pris un chemin différent ; l'un a suivi le tunnel de
gauche, l'autre celui de droite. Les traces sont encore humides et il est
probable que les deux hommes sont passés là il y a moins de vingt
minutes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez suivre les traces qui mènent dans le couloir de gauche, rendez-vous au :"))
    st.page_link("tomes/tome2/page_64.py", label="64", icon="📄")
    st.write_stream(stream_text("Si vous préférez suivre les traces qui conduisent au couloir de droite, rendez-vous au :"))
    st.page_link("tomes/tome2/page_164.py", label="164", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
