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

check_inventory(current_page_number=92, book=5)

fr_text = """
Vous courez sur les pavés, mais vous êtes bientôt contraint de
vous arrêter, car une troupe de cavaliers en uniforme apparaît
soudain au bout de la rue. En vous apercevant, ils vous chargent
à trois de front tout en poussant des cris. Maouk hurle un juron
si fort que vous êtes surpris d'entendre sa voix de tellement près,
comme s'il se trouvait à un pas de vous ! Vous vous retournez
pour l'affronter, mais il se tient toujours là où vous l'avez aperçu
au début. Il brandit une fléchette dans sa main droite et pousse
encore un juron avant de lancer son projectile dans votre
direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_25.py", label="25", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
