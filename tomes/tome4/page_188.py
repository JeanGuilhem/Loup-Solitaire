import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=188, book=4)

fr_text = """
Vous donnez l'ordre à vos hommes de creuser des tombes pour y
enterrer les deux corps, puis vous retournez à l'abri du dôme de
marbre. Vous avez faim et il vous faut à présent prendre un
Repas sinon vous perdrez 3 points d'ENDURANCE. Des
sentinelles sont postées autour du temple en ruine et vous vous
préparez à une nuit de sommeil dont vous avez grand besoin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_233.py", label="233", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
