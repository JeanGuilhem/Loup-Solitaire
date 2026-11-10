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

check_inventory(current_page_number=89, book=7)

fr_text = """
Vous sentez que le pont sera assez solide pour supporter votre
poids à condition, toutefois, qu'il ne soit pas soumis à un choc
brutal ou inattendu. Or il est possible qu'un tel choc survienne à
tout moment, étant donné les nombreuses fissures qui
l'affaiblissent. Maintenant que vous savez clairement ce qu'il en
est, vous posez un pied sur le pont et vous avancez avec d'infinies
précautions.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_243.py", label="243", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
