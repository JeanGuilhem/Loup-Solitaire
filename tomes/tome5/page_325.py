import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=325, book=5)

fr_text = """
Après avoir pris soin de recharger correctement la sarbacane,
vous portez cette arme inhabituelle à votre bouche et vous visez :
la sentinelle se tient debout, sans bouger, et constitue une cible
idéale. Vous gonflez les joues et vous soufflez puissamment.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("FLÈCHE DE SOMMEIL")
    st.caption("Vous avez utilisé une Flèche de Sommeil.")

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez la Discipline Kaï de la Maîtrise des Armes (quelle que soit l'arme), ajoutez 2 points au chiffre que vous avez tiré."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 2 if has_kai("La Maîtrise des Armes") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
        if total <= 3:
            st.write_stream(stream_text('Si le résultat obtenu est compris entre 0 et 3, rendez-vous au :'))
            st.page_link("tomes/tome5/page_384.py", label="384", icon="📄")
        else:
            st.write_stream(stream_text('Si le résultat obtenu est supérieur ou égal à 4, rendez-vous au :'))
            st.page_link("tomes/tome5/page_398.py", label="398", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
