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

check_inventory(current_page_number=183, book=3)

fr_text = """
Vous courez vers le couloir orienté au nord aussi vite que votre
cheville tordue vous le permet.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, ajoutez 2 au chiffre que vous aurez tiré.'))
    roll = hazard_roll()
    if roll is not None:
        value = roll
        if has_kai("La Chasse"):
            value += 2
            st.write(f"*Chasse : +2, total {value}.*")
        if value <= 3:
            st.write_stream(stream_text('Si le total obtenu est de 0 à 3, rendez-vous au :'))
            st.page_link("tomes/tome3/page_89.py", label="89", icon="📄")
        else:
            st.write_stream(stream_text('Si ce total est de 4 à 11, rendez-vous au :'))
            st.page_link("tomes/tome3/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
