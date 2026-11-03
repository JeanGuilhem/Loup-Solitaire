import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=319, book=4)

fr_text = """
Le Repas est délicieux. Vous mangez votre content, puis vous
vous préparez à une bonne nuit de sommeil. Lorsque l'aube se
lève, vos hommes et vous-même faites vos adieux aux
troubadours, et vous poursuivez votre voyage en direction de
Ruanon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    roll = hazard_roll()
    if roll is not None:
        if roll <= 4:
            st.write_stream(stream_text("Si vous tirez un chiffre de 0 à 4, rendez-vous au :"))
            st.page_link("tomes/tome4/page_25.py", label="25", icon="📄")
        else:
            st.write_stream(stream_text("De 5 à 9, rendez-vous au :"))
            st.page_link("tomes/tome4/page_171.py", label="171", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
