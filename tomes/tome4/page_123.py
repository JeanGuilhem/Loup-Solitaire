import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=123, book=4)

fr_text = """
Vous escaladez la colline boisée. Vous avez la gorge sèche et votre
cœur bat avec force comme s'il était près d'éclater, mais vous ne
voulez pas prendre le risque de ralentir votre allure. Quatre
heures passent avant que vous ne soyez certain d'avoir distancé
l'ennemi. La nuit est presque tombée lorsque vous découvrez par
hasard un étroit passage aux flancs escarpés, creusé dans la
colline pour donner accès à une galerie de mines. Pendant des
centaines d'années, les filons de la chaîne de Maaken ont
représenté tout à la fois une bénédiction et un fléau pour ceux
qui venaient ici chercher fortune. Des hommes, en effet, y ont
trouvé des richesses qui dépassaient leurs espérances les plus
insensées, tandis que d'autres ont péri sans laisser de traces dans
un labyrinthe de tunnels sombres et glacés. Vous examinez
l'entrée de la mine. Si vous parvenez à trouver l'un des tunnels
principaux, vous devriez pouvoir atteindre Ruanon par ces
souterrains. Quelques mètres plus loin, vous découvrez une
caisse de bois contenant 6 Torches et 1 Briquet d'Amadou. Les
galeries de mines sont obscures et vous aurez besoin d'au moins
une Torche pour vous éclairer. Vous avez cependant le droit d'en
prendre davantage si vous le désirez, mais rappelez-vous que
chaque Torche compte pour un objet dans votre Sac à Dos.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    for i in range(1, 7):
        pickup_button("TORCHE", key=f"torche_{i}", label="Prendre 1 Torche")
    pickup_button("BRIQUET À AMADOU", key="briquet", label="Prendre le Briquet d'Amadou")

    st.write_stream(stream_text("Faites les modifications nécessaires sur votre Feuille d'Aventure avant d'entrer dans les mines en vous rendant au :"))
    st.page_link("tomes/tome4/page_315.py", label="315", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
