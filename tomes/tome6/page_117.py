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

check_inventory(current_page_number=117, book=6)

fr_text = """
Mettant à profit votre maîtrise de cette Discipline Magnakaï,
vous examinez le sentier de la colline ainsi que la grand-route
afin d'y découvrir d'éventuelles traces. Mais, à votre grande
surprise, vous constatez qu'aucune de ces voies n'a été
empruntée durant les trois dernières heures. Cela signifie donc
que les cavaliers que vous recherchez sont encore cachés quelque
part dans le village.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez retourner à la bourgade, rendez-vous au :"))
    st.page_link("tomes/tome6/page_52.py", label="52", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous embusquer derrière les arbres alentour et attendre le passage des cavaliers, rendez-vous au :"))
    st.page_link("tomes/tome6/page_74.py", label="74", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
