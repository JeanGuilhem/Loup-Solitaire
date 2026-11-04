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

check_inventory(current_page_number=373, book=5)

fr_text = """
« J'ai trouvé ! s'écrie Banedon, en pointant l'index sur la carte de
la Mer de la Sécheresse posée sur sa propre carte du ciel. Deux
cents kilomètres à l'ouest de Bir Adalou et deux cents kilomètres
au sud de l'oasis de Bal-Loftan. » Puis il prend une plume d'oie et
inscrit : « Le Tombeau du Majhan ». Vous examinez la carte et
vous essayez d'évaluer la distance qui vous sépare de votre but.
Banedon remarque l'expression de doute qui se peint sur votre
visage et tente de vous remonter le moral : « Ne t'en fais pas,
Loup Solitaire, nous y serons avant l'aube. » Sa confiance vous
fait sourire, mais c'est plus ce qui vous attend à l'arrivée au
Tombeau que le voyage en lui-même qui vous inquiète.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_320.py", label="320", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
