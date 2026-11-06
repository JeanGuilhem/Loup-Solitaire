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

check_inventory(current_page_number=302, book=6)

fr_text = """
Les livres sont classés par rubriques et traitent de toutes sortes
de sujets. Vous essayez de trouver ceux qui parlent de la Pierre
de la Sagesse de Varetta, et tous ceux qui relatent en détail
l'histoire du Kaï ou la quête d'Aigle d'Or. Mais vous découvrez
avec surprise qu'ils ont tous été enlevés. A en juger par le
manque de poussière sur les étagères vides, ils ont été retirés il y
a moins d'un jour. Vous vous assurez qu'aucun autre livre ne
pourrait vous aider dans votre quête, puis vous quittez la
bibliothèque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez visiter le temple, rendez-vous au :'))
    st.page_link("tomes/tome6/page_320.py", label="320", icon="📄")

    st.write_stream(stream_text("Si vous préférez inspecter l'observatoire, rendez-vous au :"))
    st.page_link("tomes/tome6/page_127.py", label="127", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
