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

check_inventory(current_page_number=238, book=4)

fr_text = """
Posant vos mains sur la poitrine de l'homme blessé, vous faites
usage de vos pouvoirs de Guérison pour chasser la douleur avant
d'enlever la flèche. L'homme a eu de la chance : le projectile n'a
pas atteint d'organe vital. En quelques secondes, vous guérissez
la plaie grâce à votre Discipline Kaï et vous aidez l'homme à se
relever. Ce dernier vous contemple bouche bée, l'air stupéfait.
Vous vous tournez alors vers l'escalier dont vous montez les
marches en direction du sommet de la tour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_223.py", label="223", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
