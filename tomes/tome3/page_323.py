import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=323, book=3)

fr_text = """
Vous montez plus de cent marches avant d'arriver enfin à un
palier étroit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Sixième Sens, celle de l'Orientation ou de la Chasse, ajoutez 3 au chiffre que vous aurez tiré."))
    bonus = 3 if (has_kai("Le Sixième Sens") or has_kai("L'Orientation") or has_kai("La Chasse")) else 0
    roll = hazard_roll()
    if roll is not None:
        total = roll + bonus
        if bonus:
            st.write(f"*Votre Discipline Kaï vous donne +3, soit un total de {total}.*")
        if total <= 4:
            st.write_stream(stream_text("Si vous obtenez un total de 0 à 4, rendez-vous au :"))
            st.page_link("tomes/tome3/page_76.py", label="76", icon="📄")
        else:
            st.write_stream(stream_text("De 5 à 12, rendez-vous au :"))
            st.page_link("tomes/tome3/page_2.py", label="2", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
