import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=13, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous avancez péniblement dans l'égout dont les eaux sont
recouvertes d'une espèce de mousse noire et verdâtre où sont
englués toutes sortes de détritus et d'immondices. De gros
cafards grouillent sur les parois craquelées du tunnel. Les eaux
sales vous arrivent à la ceinture et, lorsque la couche de mousse
se rompt à la surface, des vapeurs de gaz putride s'élèvent et vous
prennent à la gorge. La puanteur qui s'en dégage est terriblement
asphyxiante et vous vous empressez de vous protéger le nez et la
bouche avec votre manteau Kaï. Soudain, un bruit de clapotis
vous prévient que les hommes de Maouk ne sont pas loin
derrière vous, aussi pressez-vous le pas. Vous n'avez progressé
que de quelques mètres lorsqu'un léger frottement vous fait
frémir: c'est le bruit caractéristique d'un reptile glissant
lentement sur la pierre. La peur qui vous étrangle se transforme
en terreur aveugle lorsque vous apercevez la créature qui
s'avance vers vous !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :'))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome5/page_187.py", label="187", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_187.py", label="187", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous ne maîtrisez pas cette Discipline, rendez-vous au :'))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome5/page_110.py", label="110", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_110.py", label="110", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
