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

check_inventory(current_page_number=306, book=3)

fr_text = """
Lorsque vous avez franchi l'arcade, vous remarquez un levier fixé
dans le mur. Vous le tirez et une porte coulisse aussitôt, fermant
le temple derrière vous. La température est plus élevée dans ce
passage et vous entendez quelque part au loin un sourd
grondement. Devant vous, vous apercevez une lueur, au bout du
sombre couloir. Cette lueur filtre à travers une ouverture proche
du sol et par laquelle vous distinguez un autre couloir, à 3 mètres
au-dessous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous glisser à travers cette ouverture et sauter dans le couloir en contrebas, rendez-vous au :"))
    st.page_link("tomes/tome3/page_206.py", label="206", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin le long du passage, rendez-vous au :"))
    st.page_link("tomes/tome3/page_6.py", label="6", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
