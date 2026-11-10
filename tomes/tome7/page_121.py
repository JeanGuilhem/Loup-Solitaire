import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=121, book=7)

fr_text = """
Le tentacule vous arrache du sol et, de seconde en seconde,
resserre son étreinte jusqu'à ce que vous puissiez à peine
respirer. Soudain, vous vous sentez précipité vers un autre bloc
de rocher qui s'ouvre en deux pour découvrir une monstrueuse
mâchoire dégoulinante de salive. La chose vous engloutit en un
clin d'œil. Votre vie et votre aventure se terminent, hélas, ici.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
