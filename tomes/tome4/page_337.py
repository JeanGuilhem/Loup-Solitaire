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

check_inventory(current_page_number=337, book=4)

fr_text = """
Bien que le feu ait complètement détruit toute inscription qui
aurait pu se trouver sur le chariot, vous parvenez malgré tout à
l'identifier: c'est l'un des chariots de la cavalerie du Sommerlund
que le capitaine Gayal et ses hommes ont escorté il y a un mois. Il
transportait un chargement de vivres dont il ne reste à présent
que des tas de cendres. Après avoir examiné soigneusement les
débris, vous remontez en selle et vous menez vos hommes en
direction du sud, le long de la grand-route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_297.py", label="297", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
