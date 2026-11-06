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

check_inventory(current_page_number=329, book=6)

fr_text = """
Une pluie de flèches s'abat sur vous et vous transperce de toute
part. Vous luttez de toutes vos forces pour vous maintenir en vie
mais la douleur est telle que vous perdez connaissance. Les
hommes du Capitaine piétinent votre corps : vous mourez sur le
pont de Tekaro.
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
