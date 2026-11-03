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

check_inventory(current_page_number=82, book=4)

fr_text = """
Vous avez parcouru un kilomètre et demi environ, lorsque vous
découvrez la carcasse d'un chariot brûlé abandonné au bord de la
route. Derrière l'épave, un sentier disparaît vers l'est en montant
dans les collines.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner le chariot, rendez-vous au :"))
    st.page_link("tomes/tome4/page_337.py", label="337", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas y prêter attention et poursuivre votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome4/page_297.py", label="297", icon="📄")

    st.write_stream(stream_text("Enfin, s'il vous semble opportun d'explorer le sentier montant dans les collines, rendez-vous au :"))
    st.page_link("tomes/tome4/page_15.py", label="15", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
