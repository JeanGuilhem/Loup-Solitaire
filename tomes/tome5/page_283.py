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

check_inventory(current_page_number=283, book=5)

fr_text = """
Les Nains ne s'offusquent pas de votre refus car ils ont déjà vu
des hommes rendus fous furieux, ou même tomber en syncope,
après avoir bu une chope de bière de Bor. Nolrim saisit la chope,
la vide d'un trait puis, du revers de la main, il essuie la mousse
qui est restée accrochée aux poils de sa barbe rousse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez demander aux Nains comment ils se sont retrouvés sous le commandement de Banedon, rendez-vous au :"))
    st.page_link("tomes/tome5/page_291.py", label="291", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre congé d'eux en leur souhaitant bonne nuit, rendez-vous au :"))
    st.page_link("tomes/tome5/page_359.py", label="359", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
