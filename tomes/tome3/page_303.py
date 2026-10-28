import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=303, book=3)

fr_text = """
Vous insérez la Clé dans la serrure et vous la tournez dans le sens
des aiguilles d'une montre. Un cliquetis vous indique que le
mécanisme fonctionne. Peu à peu, la tige de la Clé s'enfonce dans
le trou de la serrure et la Clé toute entière, vous glissant des
doigts, y disparaît bientôt. Le grand couvercle de pierre s'ouvre
alors, laissant apparaître un magnifique Casque d'Argent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("CLÉ D'ARGENT")
    st.write_stream(stream_text("Si vous souhaitez vous coiffer de ce Casque, rendez-vous au :"))
    st.page_link("tomes/tome3/page_308.py", label="308", icon="📄")
    st.write_stream(stream_text("Si vous préférez le laisser là où il est, vous pouvez à présent poursuivre votre chemin en montant l'escalier. Rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
