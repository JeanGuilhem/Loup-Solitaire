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

check_inventory(current_page_number=173, book=5)

fr_text = """
A en juger par la direction du courant, le canal droit semble
couler vers le nord. Le flot important des eaux usées, chargées
des immondices du Baga-Darooz, coule vers la côte, jusqu'à ce
qu'il émerge à Chivas, un village situé au nord-ouest de la
capitale. Le déversement des eaux de l'égout dans la mer rend la
vie des pauvres pêcheurs du village difficile et désagréable
(particulièrement pendant les mois d'été). Si vous suivez le canal
nord, vous atteindrez donc la côte. Le canal de gauche coule vers
le sud et passe au cœur de la ville. Dans le dédale de canaux qui
sillonnent le Baga-Darooz, vous devriez pouvoir trouver au
moins une sortie vers les rues du centre. Droit devant vous, le
canal du milieu va vers l'ouest. C'est de loin le moins pollué et le
moins fétide des trois. Vous vous rappelez qu'au cours de vos
voyages, l'homme surnommé le putois vous avait parlé du Grand
Madani, un aqueduc long de plus de 70 kilomètres qui draine
l'eau fraîche de la rivière Da vers la cité. Les citoyens de
Barrakeesh, contrairement à ceux des autres villes de
Vassagonie, jouissent donc d'un approvisionnement d'eau pure
presque illimité. Le canal ouest devrait vous conduire à la source
de la rivière Da.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez suivre le canal nord, rendez-vous au :'))
    st.page_link("tomes/tome5/page_145.py", label="145", icon="📄")

    st.write_stream(stream_text('Si vous souhaitez suivre le canal sud, rendez-vous au :'))
    st.page_link("tomes/tome5/page_96.py", label="96", icon="📄")

    st.write_stream(stream_text('Si vous souhaitez suivre le canal ouest, rendez-vous au :'))
    st.page_link("tomes/tome5/page_13.py", label="13", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
