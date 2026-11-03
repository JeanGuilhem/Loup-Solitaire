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

check_inventory(current_page_number=252, book=4)

fr_text = """
Vous menez vos hommes en file indienne dans la forêt, mais
moins d'une minute plus tard la végétation est devenue trop
dense pour que vous puissiez continuer à cheval. Vous êtes
contraints de mettre pied à terre et de cacher vos montures avant
de poursuivre votre chemin. Un peu plus tard vous avez la
chance de découvrir un étroit sentier qui mène à un hangar à
bateaux délabré, au bord de la rivière Xane. S'il y a une
embarcation dans ce hangar, vous devriez pouvoir traverser la
rivière sans difficulté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez inspecter le hangar à bateaux, rendez-vous au :'))
    st.page_link("tomes/tome4/page_68.py", label="68", icon="📄")
    st.write_stream(stream_text('Si vous préférez longer la rivière dans le sens du courant en espérant trouver un autre moyen de la franchir, rendez-vous au :'))
    st.page_link("tomes/tome4/page_130.py", label="130", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
