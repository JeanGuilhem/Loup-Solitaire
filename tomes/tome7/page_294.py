import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=294, book=7)

fr_text = """
Vous vous hissez sur la plate-forme en fer. Le labyrinthe s'étend
sous vos yeux comme la coupe d'un énorme cerveau, où chaque
cellule regorge de dangers créés par l'imagination démoniaque
du Seigneur Zahda. Un réseau de passerelles en fer reliées les
unes aux autres est suspendu au-dessus du dédale par de
gigantesques chaînes qui se perdent dans les ténèbres. Vous vous
hâtez le long d'une de ces passerelles vers un escalier qui descend
jusqu'à l'entrée d'un passage voûté situé de l'autre côté du mur
d'enceinte du labyrinthe. En dévalant les marches, vous entendez
soudain sonner une cloche d'alarme dans l'immensité au-dessus
de vous : votre fuite n'est pas passée inaperçue. Vous pénétrez
dans le passage voûté et avancez jusqu'à un croisement
comportant deux issues.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre le passage à votre droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_92.py", label="92", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre le passage à votre gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_20.py", label="20", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration, rendez-vous au :"))
    if has_magnakai("Exploration"):
        st.page_link("tomes/tome7/page_330.py", label="330", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_330.py", label="330", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
