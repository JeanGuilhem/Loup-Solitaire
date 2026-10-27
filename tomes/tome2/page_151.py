import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=151, book=2)

fr_text = """
Vous utilisez votre technique du camouflage pour imiter l'accent
rocailleux des habitants de Ragadorn et vous essayez de faire croire au
soldat qu'une bagarre a éclaté dans la rue du Tombeau. Vous affirmez
que les gardes de la ville ont été submergés par le nombre et qu'il doit
immédiatement courir à leur secours.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Vous saurez si votre mensonge a réussi en utilisant la Table de Hasard pour obtenir un "
            "chiffre. Entre 0 et 4, rendez-vous au 262. Entre 5 et 9, rendez-vous au 110."
        )
    )
    number = hazard_roll()
    if number is not None and 0 <= number <= 4:
        st.page_link("tomes/tome2/page_262.py", label="262", icon="📄")
    elif number is not None and 5 <= number <= 9:
        st.page_link("tomes/tome2/page_110.py", label="110", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
