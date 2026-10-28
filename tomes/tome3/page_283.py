import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=283, book=3)

fr_text = """
La porte se ferme rapidement et il ne vous reste guère d'espace
pour la franchir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, vous pourrez ajouter 3 au chiffre que vous aurez tiré."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + 3 if has_kai("La Chasse") else roll
        if has_kai("La Chasse"):
            st.write(f"*Chasse : {roll} + 3 = {total}.*")
        if total <= 4:
            st.page_link("tomes/tome3/page_53.py", label="53", icon="📄")
        elif total <= 7:
            st.page_link("tomes/tome3/page_16.py", label="16", icon="📄")
        else:
            st.page_link("tomes/tome3/page_113.py", label="113", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
