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

check_inventory(current_page_number=130, book=4)

fr_text = """
Pendant plus d'une heure vous suivez la berge de la rivière qui
s'enfonce dans les contreforts de la chaîne de Maaken. La rivière
Xane est large et son cours rapide. Vous n'apercevez ni pont ni
gué dans la direction où vous allez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez retourner au hangar à bateaux, rendez-vous au :'))
    st.page_link("tomes/tome4/page_68.py", label="68", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer à longer la rivière en direction de l'est, rendez-vous au :"))
    st.page_link("tomes/tome4/page_331.py", label="331", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
