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

check_inventory(current_page_number=104, book=6)

fr_text = """
Les dernières paroles de Cyrilus vous reviennent en mémoire ;
l'homme qu'il voulait vous faire rencontrer demeure dans la rue
des Chaudronniers. Mais, dans une ville de la taille de Varetta,
il vous faudrait sans doute plusieurs jours avant de découvrir
l'emplacement de cette rue. Vous décidez donc de vous informer
auprès de quelqu'un et, tout en parcourant la taverne du regard,
vous tentez de repérer un homme qui soit susceptible de vous
renseigner.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez vous approcher d'un négociant assis, seul, à la table d'à côté, rendez-vous au :"))
    st.page_link("tomes/tome6/page_240.py", label="240", icon="📄")

    st.write_stream(stream_text("Si vous préférez interroger un homme d'allure distinguée qui se tient au bar, rendez-vous au :"))
    st.page_link("tomes/tome6/page_53.py", label="53", icon="📄")

    st.write_stream(stream_text("Si vous voulez tout simplement demander des informations au tenancier de la taverne, rendez-vous au :"))
    st.page_link("tomes/tome6/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
