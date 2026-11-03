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

check_inventory(current_page_number=245, book=4)

fr_text = """
Deux coups bien ajustés suffisent à abattre les Elix. Le
patrouilleur s'est effondré sur le sol; il a perdu beaucoup de sang
et s'est presque évanoui. Son pied gauche est à demi sectionné à
hauteur de la cheville. De toute évidence, il n'a plus que quelques
minutes à vivre et vous ne pouvez rien faire pour l'aider. L'autre
patrouilleur étant déjà mort, vous êtes seul désormais.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez à présent vous enfuir en montant l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome4/page_346.py", label="346", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter les lieux en descendant l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome4/page_83.py", label="83", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
