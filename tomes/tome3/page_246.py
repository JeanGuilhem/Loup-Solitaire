import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=246, book=3)

fr_text = """
Vous abaissez le levier et la porte de pierre coulisse latéralement,
révélant une vaste grotte froide, sale et vide, à l'exception d'un
coffre de granit posé contre le mur situé à l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner ce coffre, rendez-vous au :"))
    st.page_link("tomes/tome3/page_45.py", label="45", icon="📄")
    st.write_stream(
        stream_text(
            "Si vous préférez ne pas prêter attention à cette grotte et poursuivre votre chemin en montant "
            "l'escalier, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
