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

check_inventory(current_page_number=87, book=3)

fr_text = """
Vous vous précipitez vers l'endroit où se trouvait la créature
lorsque vous l'avez aperçue, mais vous ne découvrez rien, sinon
que le couloir tourne brusquement vers l'ouest. Quelques mètres
plus loin, un escalier mène à une arcade plongée dans l'ombre, à
une dizaine de mètres au-dessus du sol. Au-delà de l'escalier, le
couloir se prolonge jusqu'à une autre porte de pierre à côté de
laquelle un levier est fixé dans le mur.
Ce levier a été relevé et la porte est fermée. Il n'y a plus trace de
l'étrange créature.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez monter l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄")

    st.write_stream(stream_text('Si vous préférez ouvrir la porte pour examiner la pièce qui se trouve derrière, rendez-vous au :'))
    st.page_link("tomes/tome3/page_246.py", label="246", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
