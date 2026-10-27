import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=172, book=2)

fr_text = """
Grâce à votre Sixième Sens, vous devinez qu'un péril vous menace
dans l'ombre de cette plate-forme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez malgré tout monter les marches et affronter ce danger, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_52.py", label="52", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez vous éloigner rapidement de ces marches et de cette plate-forme, rendez-"
            "vous au :"
        )
    )
    st.page_link("tomes/tome2/page_256.py", label="256", icon="📄")

    st.write_stream(
        stream_text(
            "Enfin, si vous choisissez de revenir en courant jusqu'au croisement pour prendre le tunnel"
            " de gauche, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_64.py", label="64", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
