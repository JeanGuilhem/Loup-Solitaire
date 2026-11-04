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

check_inventory(current_page_number=107, book=5)

fr_text = """
Vous concentrez votre pouvoir de guérison pour soigner vos
poumons atteints. Graduellement, la douleur que vous ressentez
à la poitrine disparaît et vous sentez qu'une douce chaleur
bienfaisante se répand dans vos membres. Votre Discipline Kaï a
guéri la blessure, mais vous êtes toujours très affaibli par la perte
de sang.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez fouiller le corps des Gardes, rendez-vous au :"))
    st.page_link("tomes/tome5/page_102.py", label="102", icon="📄")

    st.write_stream(stream_text("Si vous préférez laisser les corps et vous enfuir par le couloir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_150.py", label="150", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
