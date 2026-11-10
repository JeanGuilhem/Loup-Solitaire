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

check_inventory(current_page_number=329, book=7)

fr_text = """
Vous examinez le problème pendant plusieurs minutes en
utilisant au mieux vos instincts Kaï naturels pour essayer de
découvrir le nombre qui ouvrira la herse. L'image de quatre
chiffres : 3, 9, 13 et 33 vous apparaît mentalement mais, malgré
tous vos efforts, vous ne parvenez pas à savoir lequel est le bon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez tourner l'aiguille sur le chiffre 3 avant d'abaisser le levier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_3.py", label="3", icon="📄")
    st.write_stream(stream_text("Si vous voulez tourner l'aiguille sur le chiffre 9, rendez-vous au :"))
    st.page_link("tomes/tome7/page_9.py", label="9", icon="📄")
    st.write_stream(stream_text("Si vous voulez tourner l'aiguille sur le chiffre 13, rendez-vous au :"))
    st.page_link("tomes/tome7/page_13.py", label="13", icon="📄")
    st.write_stream(stream_text("Si vous voulez tourner l'aiguille sur le chiffre 33, rendez-vous au :"))
    st.page_link("tomes/tome7/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
