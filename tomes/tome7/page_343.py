import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=343, book=7)

fr_text = """
Des torches fixées aux quatre murs éclairent vivement la pièce, et
il y a peu de meubles derrière lesquels vous pouvez vous cacher.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll(key="cachette", label="Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Invisibilité, ajoutez 3 au chiffre obtenu.")
    if roll is not None:
        bonus = 3 if has_magnakai("Invisibilité") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Invisibilité : {roll} + 3 = **{total}**.*")
        st.write_stream(stream_text("Si votre total est égal ou inférieur à 7, rendez-vous au :"))
        st.page_link("tomes/tome7/page_69.py", label="69", icon="📄", disabled=total > 7)
        st.write_stream(stream_text("S'il est supérieur ou égal à 8, rendez-vous au :"))
        st.page_link("tomes/tome7/page_197.py", label="197", icon="📄", disabled=total <= 7)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
