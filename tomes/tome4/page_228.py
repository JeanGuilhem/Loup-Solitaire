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

check_inventory(current_page_number=228, book=4)

fr_text = """
L'escalier mène à un niveau inférieur où un tunnel est orienté au
sud. Vous suivez ce nouveau souterrain pendant presque un
kilomètre et demi, et vous arrivez alors dans une grande salle.
D'énormes tonneaux sont alignés contre le mur ouest et vous
apercevez dans le mur du fond une porte aménagée sous un large
escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez traverser cette salle en direction de la porte, rendez-vous au :'))
    st.page_link("tomes/tome4/page_23.py", label="23", icon="📄")

    st.write_stream(stream_text("Si vous préférez emprunter l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome4/page_105.py", label="105", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
