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

check_inventory(current_page_number=140, book=5)

fr_text = """
Les grilles de fer de l'Armurerie ne sont pas verrouillées. Vous
poussez le battant gauche et la porte tourne sur ses gonds avec
un grincement aigu qui vous fait tressaillir. Vous pénétrez à
l'intérieur ; au fond de la pièce se trouve un établi recouvert de
toutes sortes de pièces d'armurerie : fers de lance, gardes
d'épées... Au beau milieu de cet enchevêtrement, vous apercevez
un grand livre noir relié en cuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez ouvrir ce livre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_83.py", label="83", icon="📄")

    st.write_stream(stream_text("Si vous préférez laisser le livre et partir à la recherche de l'équipement que l'on vous a confisqué, rendez-vous au :"))
    st.page_link("tomes/tome5/page_181.py", label="181", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
