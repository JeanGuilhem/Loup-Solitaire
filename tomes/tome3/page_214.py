import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=214, book=3)

fr_text = """
Malheureusement, le Languabarb a décelé votre odeur et se
précipite vers votre cachette. Il vous donne un coup de son
énorme patte et ses griffes déchirent la manche de votre tunique.
Vous perdez 2 points d'ENDURANCE. Pour fuir le Languabarb, il
ne vous reste plus à présent qu'un seul moyen : traverser le lac en
courant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text("Si vous souhaitez tenter cette fuite à travers le lac, rendez-vous au :"))
    st.page_link("tomes/tome3/page_322.py", label="322", icon="📄")
    st.write_stream(stream_text("Si vous préférez combattre le Languabarb, rendez-vous au :"))
    st.page_link("tomes/tome3/page_123.py", label="123", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
