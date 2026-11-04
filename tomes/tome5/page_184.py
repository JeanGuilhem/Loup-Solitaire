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

check_inventory(current_page_number=184, book=5)

fr_text = """
Vous scrutez l'horizon et vous apercevez au fond du port un
entrepôt au toit blanc en forme de dôme. Le dernier étage du
bâtiment est prolongé par une plateforme qui surplombe le pont
d'un bateau de commerce ancré près des quais, quelques mètres
plus bas. Sur cette plate-forme se trouvent de grosses amphores
en terre cuite, remplies d'épices, qui doivent être chargées à bord
du navire pour être livrées aux comptoirs commerciaux de
Ragadorn. Vous fixez votre attention sur une amphore puis vous
essayez, à l'aide de votre Discipline Kaï, de la faire bouger. Ce
violent effort de concentration vous fait suer abondamment et
des gouttes commencent à perler sur votre front. Quelques
secondes plus tard, vous entendez un choc au loin : vous avez
réussi; l'amphore a oscillé, puis est tombée sur le pont du navire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_153.py", label="153", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
