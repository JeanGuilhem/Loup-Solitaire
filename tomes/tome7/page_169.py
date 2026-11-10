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

check_inventory(current_page_number=169, book=7)

fr_text = """
Le mur s'abaisse de plus en plus vite ; il ne reste déjà presque plus
assez de place pour passer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, ajoutez 3 au chiffre que vous avez tiré."))
    roll = hazard_roll(key="mur")
    if roll is not None:
        total = roll + (3 if has_magnakai("Art de la Chasse") else 0)
        if total != roll:
            st.write(f"*Art de la Chasse : +3, soit un total de {total}.*")
        st.write_stream(stream_text("Si le résultat est compris entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome7/page_237.py", label="237", icon="📄", disabled=total > 4)
        st.write_stream(stream_text("Si ce résultat est supérieur ou égal à 5, rendez-vous au :"))
        st.page_link("tomes/tome7/page_326.py", label="326", icon="📄", disabled=total < 5)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
