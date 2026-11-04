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

check_inventory(current_page_number=44, book=5)

fr_text = """
Vous entrez rapidement par la porte ouest et vous vous engagez
dans un couloir agréablement frais. Au dos de la porte, une
grosse barre de fer attire votre attention. Vous la tirez afin de
retarder d'éventuels poursuivants. Au bout du couloir se trouve
une salle d'armes. Des râteliers garnis de lances et d'épées
s'étendent sur tous les murs et un établi massif se dresse au
centre de la pièce. Vous vous trouvez dans l'Armurerie du Palais !
Parmi les nombreux outils qui encombrent l'établi, il y a un
grand livre relié en cuir noir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez feuilleter ce livre, rendez-vous au :'))
    st.page_link("tomes/tome5/page_83.py", label="83", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous mettre à la recherche de l'équipement que l'on vous a confisqué, sans vous occuper de ce livre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_181.py", label="181", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
