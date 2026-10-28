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

check_inventory(current_page_number=54, book=3)

fr_text = """
Le verre est très fin et vous avez besoin de toute votre
concentration et de toute votre habileté pour éviter de le casser.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez la Discipline Kaï de la "
            "Maîtrise Psychique de la Matière ou celle de la Puissance Psychique, ajoutez 3 au chiffre que "
            "vous aurez tiré."
        )
    )
    roll = hazard_roll()
    if roll is not None:
        bonus = 3 if has_kai("Maîtrise Psychique de la Matière") or has_kai("Puissance psychique") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Votre Discipline Kaï vous donne +{bonus} : total {total}.*")
        if total <= 4:
            st.write_stream(stream_text("Votre total est de 0 à 4, rendez-vous au :"))
            st.page_link("tomes/tome3/page_250.py", label="250", icon="📄")
        else:
            st.write_stream(stream_text("Votre total est de 5 à 12, rendez-vous au :"))
            st.page_link("tomes/tome3/page_268.py", label="268", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
