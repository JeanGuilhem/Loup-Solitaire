import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_magnakai,
    magnakai_rank,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=172, book=7)

fr_text = """
Vous êtes entraîné hors de la pièce sous la pression de l'eau et
vous vous retrouvez par terre, au pied d'une rampe fortement
inclinée. Vous vous essuyez les yeux et regardez autour de vous
avec une vive inquiétude. La porte ovale se referme brusquement
derrière vous dans un claquement sonore qui se répercute en
s'amplifiant le long de l'immense couloir. Les murs de ce dernier
sont recouverts de gigantesques cocons, et vous apercevez
soudain à quelques mètres une forme qui bouge dans l'obscurité.
Une créature ressemblant à un énorme ver, pourvue de deux gros
yeux noirs et de mandibules cornées, rampe dans votre direction !
Une écume violette s'échappe en bouillonnant de sa bouche
tandis qu'elle se rapproche rapidement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    invisibility = has_magnakai("Invisibilité")
    # rang de Maître Primat : 4 Disciplines Magnakaï
    animal_control = has_magnakai("Contrôle Animal") and magnakai_rank() >= 4
    whistle = has_item("SIFFLET D'ARGENT")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Invisibilité, rendez-vous au :"))
    if invisibility:
        st.page_link("tomes/tome7/page_86.py", label="86", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_86.py", label="86", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï du Contrôle Animal et si vous avez atteint le rang de Maître Primat, rendez-vous au :"))
    if animal_control:
        st.page_link("tomes/tome7/page_130.py", label="130", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_130.py", label="130", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous avez un Sifflet d'Argent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_347.py", label="347", icon="📄", disabled=not whistle)

    st.write_stream(stream_text("Si vous ne maîtrisez aucune de ces Disciplines et si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    st.page_link("tomes/tome7/page_233.py", label="233", icon="📄", disabled=invisibility or animal_control or whistle)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
