import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=266, book=6)

fr_text = """
La bière est onctueuse et rafraîchissante. (Vous regagnez 1 point
d'ENDURANCE.) Pendant que vous buvez, le garçon reste affalé sur
son tabouret à moitié endormi, totalement indifférent à votre
présence. Vous finissez votre chope que vous reposez brusquement
sur le comptoir, espérant ainsi le tirer de sa torpeur mais il
reste sans réaction. Cependant, vous ne voulez pas quitter la
cabane sans le remercier pour son hospitalité.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=1)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_93.py", label="93", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
