import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=3, book=6)

fr_text = """
Au sommet de la colline, le sentier se termine brusquement par un
grand cercle de pierres. Un fagot de bois est posé en plein
milieu, à côté d'une Torche enveloppée de toile huilée. Vous
reconnaissez là un signe de piste. Ce genre de balise est en effet
très fréquent au Sommerlund, et particulièrement le long de la
frontière qui borde les Monts Durncrag. Si vous le désirez, vous
pouvez prendre cette Torche avant de rebrousser chemin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("TORCHE", key="torche", label="Prendre la Torche")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_330.py", label="330", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
