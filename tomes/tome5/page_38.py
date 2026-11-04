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

check_inventory(current_page_number=38, book=5)

fr_text = """
Vous avez à moitié contourné la petite tour lorsqu'une pierre de
la corniche commence à s'effriter sous vos pieds. Vous levez
instinctivement les bras et vous parvenez à vous agripper au
rebord en surplomb. En dessous, le vide est terrifiant, mais
malgré votre effroi, vous trouvez l'énergie et la force nécessaire
pour reprendre votre prise sur la corniche. Vos mains sont en
sang, mais vous avez la vie sauve ! Épuisé par cet effort, vous
perdez 1 point d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text('Rendez-vous maintenant au :'))
    st.page_link("tomes/tome5/page_87.py", label="87", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
