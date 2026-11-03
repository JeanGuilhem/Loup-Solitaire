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

check_inventory(current_page_number=328, book=4)

fr_text = """
Lorsque vous parvenez au sommet du monticule, un spectacle
sinistre s'offre à vos yeux. Des cadavres d'hommes et de chevaux
jonchent une vallée peu profonde qui s'étend devant vous. Les
corbeaux sont en train de déchiqueter leurs restes, ne laissant
plus que des ossements nus. Vos patrouilleurs ne peuvent retenir
des exclamations horrifiées lorsqu'ils reconnaissent les armures
et les uniformes en lambeaux dont sont encore vêtus certains de
ces squelettes. Ces hommes, en effet, étaient des soldats de la
cavalerie royale du Sommerlund. Sans doute sont-ils morts en
livrant bataille, car des cadavres de Guerriers Pillards sont
également étendus à leurs côtés. Quarante vaillants soldats, c'est-
à-dire presque la moitié de l'escadron qui a quitté Holmgard il y
a un mois, reposent ainsi devant vous. Le cœur lourd, vos
patrouilleurs entreprennent alors la triste tâche de leur offrir une
sépulture décente. Une fois cette besogne accomplie, vous quittez
cette vallée de la mort en n'éprouvant qu'un seul réconfort : le
capitaine Gayal ne faisait pas partie des cadavres que vous avez
enterrés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_120.py", label="120", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
