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

check_inventory(current_page_number=243, book=4)

fr_text = """
Le capitaine Gayal passe devant le chariot à la tête d'une
douzaine de ses meilleurs soldats et lance une contre-offensive
qui repousse l'ennemi jusqu'à la barricade. Il n'y a pas de
survivants chez vos adversaires. Ceux qui ont réussi à échapper
aux soldats du capitaine sont en effet abattus par les archers,
tandis qu'ils s'enfuient dans la plaine pour tenter vainement de
se réfugier parmi les ruines. Un cri de victoire s'élève sur le
champ de bataille, mais à peine ses derniers échos se sont-ils
envolés qu'un nouveau danger vous menace.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_124.py", label="124", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
