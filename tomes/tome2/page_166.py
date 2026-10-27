import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=166, book=2)

fr_text = """
Vous montez un escalier et vous vous retrouvez sur le pont du navire ;
la bataille fait rage tandis que les vaisseaux fantômes encerclent la
flotte de Durenor. Soudain, un éclair de feu jaillit d'une tour dressée à
l'arrière du bateau fantôme sur lequel vous vous trouvez, et vient
frapper dans une gigantesque explosion le flanc d'un navire de la flotte
durnoraise, à moins de 50 mètres de distance. Vous voyez alors avec
horreur les soldats alliés sauter du pont, leurs vêtements et leurs
cheveux en flammes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez explorer cette tour, rendez-vous au :"))
    st.page_link("tomes/tome2/page_328.py", label="328", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous enfuir en sautant par-dessus bord, rendez-vous au :"))
    st.page_link("tomes/tome2/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
