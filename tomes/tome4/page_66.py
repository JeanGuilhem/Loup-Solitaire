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

check_inventory(current_page_number=66, book=4)

fr_text = """
Vous atterrissez sur le sol en roulant sur vous-même. Le
Vassagonien bondit à votre suite, espérant vous porter un coup
mortel avant que vous n'ayez pu vous relever. Mais il ne semble
pas se rendre compte qu'il a affaire à un Seigneur Kaï. Vous le
frappez, en effet, alors qu'il n'a pas encore touché terre et il
s'effondre à côté de vous, tué sur le coup. Le capitaine Gayal
passe en courant à votre gauche. Il mène une contre-offensive à
la tête de ses meilleurs combattants et repousse l'ennemi vers la
barricade. Bientôt les lignes adverses sont anéanties et les
attaquants qui ont survécu aux coups portés par les soldats du
capitaine sont abattus par ses archers, tandis qu'ils tentent de
s'enfuir dans la plaine. Mais à peine le cri de victoire des soldats
du Sommerlund a-t-il retenti qu'il vous faut faire face à une
nouvelle et redoutable attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_124.py", label="124", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
