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

check_inventory(current_page_number=77, book=5)

fr_text = """
Votre bras paralysé rend l'ascension impossible. Sans faiblir,
vous essayez courageusement de vous échapper par la cheminée,
mais soudain un fragment de roche se détache sous votre main et
vous tombez à la renverse dans la boue en ébullition. Vous
trouvez une mort atroce, mais rapide, dans le tar-sorkh de Barrakeesh.
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
