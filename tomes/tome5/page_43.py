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

check_inventory(current_page_number=43, book=5)

fr_text = """
Vous atteignez une petite pièce construite au-dessus du tunnel.
Dans cet endroit au moins, l'air est sec, bien que les vapeurs
fétides de l'égout parviennent encore jusqu'à vos narines. Vous
vous éloignez rapidement par un étroit passage qui tourne une
première fois vers l'ouest, puis vers le sud. Mais vous sentez votre
cœur défaillir en constatant, malgré l'obscurité, que vous êtes
dans une impasse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez examiner plus attentivement les lieux pour tenter de découvrir une issue dérobée, rendez-vous au :'))
    st.page_link("tomes/tome5/page_33.py", label="33", icon="📄")
    st.write_stream(stream_text('Si vous préférez vous préparer à combattre, rendez-vous au :'))
    st.page_link("tomes/tome5/page_185.py", label="185", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
