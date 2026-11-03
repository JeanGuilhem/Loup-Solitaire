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

check_inventory(current_page_number=55, book=4)

fr_text = """
La voie ferrée suit un tunnel éclairé par des Torches. Vous passez
devant des chariots de mine qui portent tous la même marque
sur leurs flancs de bois : une croix ancrée surmontant les initiales
O.V. Il s'agit là du sceau d'Oren Vanalund, baron de Ruanon.
Cette découverte vous confirme que vous avez pris la bonne
direction. Soudain, des bruits de pas retentissent dans le tunnel,
s'approchant de vous. Ils deviennent de plus en plus sonores et
s'accompagnent de cris et de claquements de fouet.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous cacher dans l'un des chariots vides, rendez-vous au :"))
    st.page_link("tomes/tome4/page_161.py", label="161", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous dissimuler dans l'ombre des murs du tunnel, rendez-vous au :"))
    st.page_link("tomes/tome4/page_286.py", label="286", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
