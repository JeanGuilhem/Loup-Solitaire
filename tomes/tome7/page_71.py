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

check_inventory(current_page_number=71, book=7)

fr_text = """
A moitié aveuglé par les émanations, vous ne vous apercevez pas
qu'il y a un fil tendu en travers du couloir, à hauteur du genou.
Dès que vous l'effleurez de la jambe, votre remarquable instinct
de survie vous prévient du piège. Le plafond se met à trembler et,
simultanément, deux murs de pierre commencent à s'abaisser,
menaçant d'obstruer le tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez plonger sous le mur qui s'abaisse en face de vous avant qu'il ne soit trop tard, rendez-vous au :"))
    st.page_link("tomes/tome7/page_337.py", label="337", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous glisser rapidement sous le mur qui descend derrière vous, rendez-vous au :"))
    st.page_link("tomes/tome7/page_169.py", label="169", icon="📄")

    st.write_stream(stream_text("Si vous jugez préférable de rester là où vous vous trouvez, rendez-vous au :"))
    st.page_link("tomes/tome7/page_37.py", label="37", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
