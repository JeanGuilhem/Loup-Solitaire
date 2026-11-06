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

check_inventory(current_page_number=263, book=6)

fr_text = """
« Que... que... que me voulez-vous ? » glousse le marchand apeuré
en se blottissant derrière la table. Ses manières hautaines ont
complètement disparu depuis que ses gardes du corps sont morts, et
il tremble de tous ses membres. Vous poussez la table sur le côté
puis vous le relevez par le revers de son habit et vous lui dites
en riant: « Du calme, l'ami ! Je désire simplement savoir où se
trouve la rue des Chaudronniers. » Le marchand vous regarde
incrédule, de grosses gouttes de sueur coulant sur son visage
couleur de cendre. « Le... le chemin de la rue des Chaudronniers ?
bégaie-t-il. Mais bien sûr, bien sûr... m'sieur... voilà... » Le
petit homme, terrifié, sort de sa poche un morceau de parchemin
jauni et, d'un index tremblant, s'empresse de vous indiquer le
chemin à suivre. La rue est située à l'autre bout de la ville près
du mur d'enceinte ouest. Vous lui prenez le parchemin des mains,
puis vous lui souhaitez bonne nuit, avant d'enjamber les corps des
gardes. Vous entendez un bruit sourd derrière vous: le marchand a
perdu connaissance et s'est étalé de tout son long sur le sol de
la taverne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_17.py", label="17", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
