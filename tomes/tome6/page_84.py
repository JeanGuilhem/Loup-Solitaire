import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=84, book=6)

fr_text = """
Le taxidermiste désigne, dans un coin de la pièce, une cuve
contenant un liquide bleu qui, d'après l'odeur qui s'en dégage,
est responsable de la puanteur ambiante. «Voilà mon conservateur
spécial, explique-t-il fièrement. Il m'a fallu plusieurs années
pour mettre la formule au point, mais j'ai maintenant terminé
mes expériences... il ne me manque plus que de trouver un
spécimen digne de l'immortalité que je suis désormais capable de
conférer. » Peu à peu, la voix de votre hôte s'affaiblit et
semble s'éloigner, comme s'il tombait au fond d'un puits très
profond. Vos paupières sont lourdes et vous avez du mal à vous
concentrer pour saisir le sens de ses paroles. Vous comprenez
subitement que vous avez été drogué : le vin que l'homme vous a
servi contenait une forte dose d'Herbe à Potence, mais vous ne
vous en êtes malheureusement pas rendu compte à temps. Vous
luttez désespérément pour rester éveillé, mais en vain, car le
poison coule déjà dans vos veines. Le taxidermiste va enfin
pouvoir tester son fameux conservateur sur un sujet digne d'une
telle expérience : le dernier des Seigneurs Kaï du Sommerlund !
Votre aventure se termine, hélas ! ici.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
