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

check_inventory(current_page_number=227, book=4)

fr_text = """
Ces oiseaux sont des corbeaux, communs dans le Pays Sauvage
où ils se nourrissent de charognes. Lorsqu'une créature meurt,
on peut être sûr de voir apparaître bientôt sur son cadavre ces
répugnants nécrophages.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner de plus près les corps qu'ils sont en train de dévorer, rendez-vous au :"))
    st.page_link("tomes/tome4/page_328.py", label="328", icon="📄")

    st.write_stream(stream_text('Si vous préférez ne pas y prêter attention et poursuivre votre chemin, rendez-vous au :'))
    st.page_link("tomes/tome4/page_120.py", label="120", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
