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

check_inventory(current_page_number=326, book=7)

fr_text = """
L'espace se réduit maintenant à quelques centimètres, mais vous
parvenez quand même à vous glisser en dessous et vous vous
retrouvez de l'autre côté. Vous vous relevez, l'estomac noué, et
revenez sur vos pas le long du tunnel obscur. La lueur rouge que
vous aviez vue auparavant brille toujours devant vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez maintenant explorer ce tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_144.py", label="144", icon="📄")
    st.write_stream(stream_text("Si vous préférez retourner à la caverne aux parois rudimentaires et prendre le tunnel ouest, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
