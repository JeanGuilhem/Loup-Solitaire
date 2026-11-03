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

check_inventory(current_page_number=98, book=4)

fr_text = """
Le cimeterre du Guerrier siffle à quelques centimètres au-dessus
de votre tête alors que vous vous laissez tomber dans l'ouverture
de la trappe. Il essaie de vous suivre, mais les coups que vous lui
portez le forcent à reculer. Vous parvenez à refermer la trappe et
à tirer le verrou, empêchant désormais votre adversaire de
pénétrer à l'intérieur de la tour de guet. Essayant de chasser de
votre esprit les images sanglantes de la bataille, vous descendez
quatre à quatre les marches de l'escalier et vous sortez de la tour
de guet.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_59.py", label="59", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
