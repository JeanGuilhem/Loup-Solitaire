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

check_inventory(current_page_number=247, book=7)

fr_text = """
« N'ayez pas peur, dites-vous en essayant de rassurer l'homme
effrayé. Je ne vous ferai aucun mal. » Au son de votre voix, il
cesse de trembler, tourne vers vous son visage apeuré et
demande : « Ce sont les Anciens Mages qui vous ont envoyé ici ?
»
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez lui répondre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_340.py", label="340", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter la cellule sans répondre à sa question, rendez-vous au :"))
    st.page_link("tomes/tome7/page_142.py", label="142", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
