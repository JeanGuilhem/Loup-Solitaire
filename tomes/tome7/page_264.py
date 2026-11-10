import streamlit as st
from inventory import (
    check_inventory,
    confiscate_equipment,
    display_inventory,
    end_page,
    is_new_page,
    item_info,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=264, book=7)

fr_text = """
La foule hurle son approbation tandis qu'une créature bossue et
rachitique, enveloppée dans un habit à capuchon, s'approche de
l'endroit où vous êtes attaché. Elle vous débarrasse prestement
de toutes vos armes et les tend à un nain au visage hideux qui se
tient à ses côtés. « Emmenez-le dans le labyrinthe ! » ordonne le
Seigneur aux cheveux blancs. Son rire cruel et moqueur retentit à
vos oreilles tandis que des gardes vous font traverser, enchaîné,
le hall. Effacez toutes les armes et les Objets Spéciaux pouvant
servir d'armes de votre Feuille d'Aventure et notez-les sur une
feuille de papier à part, au cas où vous les retrouveriez à un stade
ultérieur de votre aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        confiscate_equipment(backpack=False, special=False, gold=False)
        # les Objets Spéciaux pouvant servir d'armes (Glaive de Sommer...) sont pris aussi
        for item in [item for item in st.session_state.special if item_info(item).get("weapon")]:
            remove_from_inventory(item)
            st.session_state.confiscated["special"].append(item)
    st.warning("On vous a pris toutes vos armes, ainsi que les Objets Spéciaux pouvant servir d'armes.")

    st.write_stream(stream_text("A présent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_286.py", label="286", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
