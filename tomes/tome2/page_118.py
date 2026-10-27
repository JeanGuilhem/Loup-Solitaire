import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=118, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous dites adieu à Rhygar et vous entrez dans le tunnel de Tarnalin.
D'une largeur et d'une hauteur de 30 mètres environ, le tunnel traverse
les montagnes de la chaîne d'Hammardal et permet d'accéder à la
capitale. Des torches l'éclairent sur toute sa longueur et les marchands
sont nombreux à l'emprunter car c'est la seule voie qui relie Port Bax à
Hammardal. D'ordinaire, la circulation y est intense mais vous
constatez avec surprise qu'il est désert au moment où vous y pénétrez ;
vous n'y trouvez qu'une carriole de fruits renversée sur la chaussée.
Vous continuez à avancer dans le tunnel et un doute alors vous saisit:
les Monstres d'Enfer seraient-ils arrivés avant vous ? Au bout d'une
heure de marche, vous apercevez une étrange créature perchée sur le
toit d'un chariot au milieu de la chaussée. L'animal mesure une
soixantaine de centimètres de haut et ressemble à un rat géant. Vous
pensez qu'il s'agit là d'un rongeur qui a établi ses quartiers dans le
tunnel, mais vous remarquez en vous approchant que la créature porte
une magnifique veste de cuir en patchwork et qu'elle tient une lance
dans sa patte. L'animal se tourne soudain vers vous lorsqu'il entend vos
pas. Les moustaches de son museau frémissent tandis qu'il renifle
alentour et ses yeux scrutent l'obscurité. Dès qu'il vous voit, il prend la
fuite et disparaît dans un tunnel plus petit situé à votre gauche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez suivre cette créature, rendez-vous au :"))
    st.page_link("tomes/tome2/page_23.py", label="23", icon="📄")
    st.write_stream(stream_text("Si vous préférez la laisser filer sans vous en soucier et poursuivre votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome2/page_340.py", label="340", icon="📄")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication animale, rendez-vous au :"))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome2/page_279.py", label="279", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_279.py", label="279", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
