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

check_inventory(current_page_number=367, book=5)

fr_text = """
Vous suivez la rue silencieusement et vous commencez à
désespérer. La ruelle est de plus en plus étroite et de plus en plus
sale. Un chat malingre se met en travers de votre chemin,
poursuivi par un gamin des rues aussi maigre que lui; le couteau
qu'il tient à la main indique clairement qu'il est en train de courir
après son dîner. Vous êtes sur le point d'abandonner et vous
proposez à Banedon de revenir sur vos pas jusqu'au croisement,
lorsque la rue fait un brusque coude sur la gauche. Une flèche
dessinée sur le mur d'en face indique la direction du marché aux
Douggas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez suivre la flèche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_376.py", label="376", icon="📄")
    st.write_stream(stream_text("Si vous préférez retourner au croisement pour prendre l'autre rue, rendez-vous au :"))
    st.page_link("tomes/tome5/page_216.py", label="216", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
