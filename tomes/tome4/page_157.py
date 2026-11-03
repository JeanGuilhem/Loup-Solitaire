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
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=157, book=4)

fr_text = """
Vous êtes à présent si fatigué qu'il vous faut à tout prix vous
arrêter et dormir. Plusieurs heures de sommeil vous permettent
de retrouver vos forces. Vous gagnez un point d'ENDURANCE et
vous poursuivez votre exploration du tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=1)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_309.py", label="309", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
