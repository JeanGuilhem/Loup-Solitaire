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

check_inventory(current_page_number=37, book=7)

fr_text = """
En l'espace de quelques secondes, toute issue est complètement
bloquée. C'est alors que vous parvient un long sifflement.
Simultanément, une odeur âcre emplit vos narines. Le temps que
vous réalisiez qu'il s'agit là d'un gaz soporifique très violent, qui
s'échappe par de minuscules trous pratiqués au-dessus du sol,
vous succombez à son irrésistible pouvoir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome7/page_165.py", label="165", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
