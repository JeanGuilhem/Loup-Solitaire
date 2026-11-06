import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=285, book=6)

fr_text = """
Devant vous, vous apercevez un autre escalier en pierre qui
descend vers les cachots du Château de Taunor. L'escalier est
plongé dans l'obscurité la plus totale, et vous commencez à
descendre avec d'infimes précautions. Une odeur épouvantable de
moisi et de décomposition vous oblige à vous boucher le nez. Le
Yamsark est toujours derrière vous, et vous pouvez entendre ses
étranges cris inhumains. Mais ses mugissements se transforment
bientôt en un rire démoniaque et strident qui vous fait frémir
d'horreur et de dégoût. Vous arrivez au bas des marches et, grâce
à vos instincts Kaï, vous sentez qu'un passage s'enfonce tout
droit et qu'à votre droite se trouve une petite niche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez continuer tout droit, rendez-vous au :"))
    st.page_link("tomes/tome6/page_192.py", label="192", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous cacher dans la niche, rendez-vous au :"))
    st.page_link("tomes/tome6/page_69.py", label="69", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
