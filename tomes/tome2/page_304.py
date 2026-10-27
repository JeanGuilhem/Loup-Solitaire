import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, ls_death, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=304, book=2)

fr_text = """
Vous éprouverez peut-être quelque consolation en apprenant que votre
mort a été quasiment instantanée. En quelques secondes, les doigts du
Monstre d'Enfer vous ont déchiré la gorge et le Sceau d'Hammardal ne
tardera pas à parvenir à Helgedad, la ville des Maîtres des Ténèbres.
Votre mission s'achève ici en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
