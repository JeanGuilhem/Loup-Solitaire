import streamlit as st
from inventory import (
    check_inventory,
    clear_flag,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# fait retiré : "cheval" (votre cheval est tué)

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=150, book=6)

fr_text = """
Votre cheval reçoit une volée de flèches qui le blessent
mortellement. Il titube, et vous vous trouvez balayé sur le côté
au passage des cavaliers et des hommes qui se ruent en criant
sur le pont. Sous la pression de cette horde déchaînée, vous
basculez soudain par-dessus le parapet et vous tombez, la tête
la première, dans les eaux glaciales de la Quarle. Le courant
tumultueux vous emporte comme un fétu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        clear_flag("cheval")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
