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

check_inventory(current_page_number=9, book=4)

fr_text = """
Vous êtes saisi de panique en sentant le pont se dérober sous vos
pieds. Vous plongez en avant et vous parvenez à attraper de
justesse l'une des planches de la passerelle. Vous êtes loin
cependant d'être tiré d'affaire. Vous sentez en effet vos mains
glisser de leur prise et, par ailleurs, le pont qui s'effondre va venir
s'écraser dans quelques instants contre le mur d'en face.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous cramponner à la passerelle et vous préparer au choc qui vous attend, rendez-vous au :"))
    st.page_link("tomes/tome4/page_112.py", label="112", icon="📄")

    st.write_stream(stream_text("Si vous préférez lâcher prise et sauter dans les profondeurs inconnues du puits de mine, rendez-vous au :"))
    st.page_link("tomes/tome4/page_342.py", label="342", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
