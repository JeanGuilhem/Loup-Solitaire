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

check_inventory(current_page_number=72, book=4)

fr_text = """
Les plates étendues du Pays Sauvage n'offrent aucun abri pour
vous cacher des brigands. Pour essayer d'éviter un combat contre
un ennemi qui vous surpasse largement en nombre, il vous faut
séparer votre troupe en deux et prendre la fuite en espérant
pouvoir distancer vos poursuivants. Vous prenez dix hommes
avec vous et vous envoyez les autres en direction de l'ouest, dans
l'espoir qu'ils attireront les brigands vers les monts Durncrag.
Vous jetez un dernier regard à l'ennemi, puis vous partez au
galop menant vos dix patrouilleurs le long de la voie de Ruanon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_211.py", label="211", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
