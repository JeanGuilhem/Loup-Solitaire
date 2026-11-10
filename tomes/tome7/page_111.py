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

check_inventory(current_page_number=111, book=7)

fr_text = """
Vous voilà dans un passage aux murs nus et lisses. Au-dessus de
vous flotte une brume scintillante qui irradie juste assez de
lumière pour que vous puissiez voir à quelques mètres devant
vous. Vous vous sentez nu et vulnérable sans vos armes, mais il
vous reste quand même votre Sac à Dos, vos Pièces d'Or et vos
Objets Spéciaux, ce qui est mieux que rien ! Vous commencez à
avancer prudemment, redoutant l'imprévisible, jusqu'à ce que
vous arriviez à une cave circulaire. Là, en plein milieu, se dresse
un bloc de marbre sur lequel est posée une épée en acier. Au
moment où vous franchissez le seuil de la pièce, vous apercevez
des dalles de pierre s'enfonçant dans le sol et découvrant deux
issues : l'une à votre gauche, l'autre à droite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition ou de l'Écran Psychique, rendez-vous au :"))
    if has_magnakai("Intuition") or has_magnakai("Écran Psychique"):
        st.page_link("tomes/tome7/page_68.py", label="68", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_68.py", label="68", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous voulez prendre l'épée qui se trouve devant vous, rendez-vous au :"))
    st.page_link("tomes/tome7/page_224.py", label="224", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez sortir de cet endroit en empruntant le tunnel de gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_298.py", label="298", icon="📄")

    st.write_stream(stream_text("Si vous préférez partir par le tunnel de droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
