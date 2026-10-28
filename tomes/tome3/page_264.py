import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=264, book=3)

fr_text = """
Vous entrez dans une grande salle mal éclairée où règne un froid
glacial : c'est un temple secret construit là par les Anciens. Le sol
est recouvert de dalles de quartz et de granite; des pierres et des
morceaux de glace sont répandus çà et là. Délimitée par deux
rangées de hauts piliers, une allée mène à un autel sacrificatoire
aménagé dans une alcôve du mur situé au nord. Sur cet autel
repose une étrange statue qui semble avoir été sculptée dans de
la pierre blanche et lisse. A la tête et aux pieds de la statue, se
dressent des piliers noirs encastrés dans la pierre de l'autel. A la
gauche de la statue, un escalier monte vers une arcade plongée
dans l'ombre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez traverser le temple en direction de l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome3/page_60.py", label="60", icon="📄")

    st.write_stream(stream_text('Si vous voulez traverser le temple en ne marchant que sur les dalles de quartz, rendez-vous au :'))
    st.page_link("tomes/tome3/page_168.py", label="168", icon="📄")

    st.write_stream(stream_text('Si vous préférez traverser le temple en ne marchant que sur les dalles de granite, rendez-vous au :'))
    st.page_link("tomes/tome3/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
