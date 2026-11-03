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

check_inventory(current_page_number=347, book=4)

fr_text = """
Vous êtes arrivé au fond de la cave, lorsque la trappe se referme
soudain. Vous entendez qu'on la verrouille, et vous vous mettez à
frapper le panneau à coups redoublés, essayant désespérément
de vous échapper. Ceux qui vous ont ainsi enfermé condamnent
la trappe à l'aide d'un énorme tonneau. Des Gardes restent dans
la cabane pour surveiller votre prison. Quatre jours se passent
avant que la trappe ne s'ouvre à nouveau. C'est alors la main
décharnée d'un squelette qui rabat le panneau de bois. Les morts
de Maaken se sont réveillés. Votre mission a échoué.
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
