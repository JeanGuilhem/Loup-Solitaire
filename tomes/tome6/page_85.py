import streamlit as st
from inventory import (
    can_shoot,
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=85, book=6)

fr_text = """
En entendant le déclic de la détente de l'arbalète, vous vous
jetez à terre pour éviter le projectile meurtrier. Le carreau
vous érafle le cuir chevelu (vous perdez 2 points d'ENDURANCE)
et va ensuite se planter dans la hutte en rondins. Quelques
instants plus tard, vous vous remettez debout et vous voyez le
guerrier éperonner son cheval pour rejoindre ses compagnons, de
l'autre côté du pont.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous possédez un arc, rendez-vous au :"))
    st.page_link("tomes/tome6/page_178.py", label="178", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous n'en avez pas, enfourchez vite votre monture et lancez-vous à la poursuite des cavaliers. Rendez-vous au :"))
    if can_shoot():
        st.page_link("tomes/tome6/page_39.py", label="39", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_39.py", label="39", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
