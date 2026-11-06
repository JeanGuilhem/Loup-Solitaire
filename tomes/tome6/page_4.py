import streamlit as st
from combat import combat_weapons
from inventory import (
    check_inventory,
    choose_item_to_lose,
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

check_inventory(current_page_number=4, book=6)

fr_text = """
Alors que vous écartez les filaments, ceux-ci se mettent soudain à
frémir à votre contact et à se contorsionner comme des serpents.
Puis ils s'enroulent autour de votre arme et la retournent contre
vous ! Vous lâchez aussitôt prise et vous reculez rapidement,
horrifié, en voyant la lame se désagréger sous l'effet de la
substance corrosive distillée par les filaments. Faisant
volte-face, vous retournez en courant vers l'embranchement,
l'estomac noué d'effroi en réalisant, rétrospectivement, que vous
venez de frôler de très près une mort atroce ! (N'oubliez pas de
rayer l'arme que vous avez perdue sur votre Feuille d'Aventure.) A
présent, quelle direction allez-vous prendre ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'arme qui a servi à écarter les filaments est détruite (l'Arc ne sert pas à cela)
    if choose_item_to_lose(combat_weapons(), key="arme_filaments", label="Choisissez l'arme avec laquelle vous avez écarté les filaments :"):
        st.write_stream(stream_text("Si vous optez pour le tunnel de gauche, rendez-vous au :"))
        st.page_link("tomes/tome6/page_269.py", label="269", icon="📄")

        st.write_stream(stream_text("Si vous préférez aller tout droit, rendez-vous au :"))
        st.page_link("tomes/tome6/page_339.py", label="339", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
