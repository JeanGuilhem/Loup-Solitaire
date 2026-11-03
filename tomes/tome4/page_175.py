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

check_inventory(current_page_number=175, book=4)

fr_text = """
Vous avez parcouru un peu plus d'un kilomètre, lorsqu'une
catastrophe se produit : devant vous, un patrouilleur pousse
soudain un cri perçant ; un disque d'acier aux bords acérés s'est
enfoncé dans sa poitrine. D'autres disques mortels sifflent
aussitôt en tous sens.
Pour éviter que tous vos hommes soient abattus par vos
agresseurs invisibles, vous les menez au galop dans une fuite
éperdue. Lorsque vous tirez enfin sur les rênes de votre cheval
aux flancs ruisselants d'écume, vous êtes à plus de 3 kilomètres
de l'endroit où l'embuscade a été tendue. Il ne vous reste hélas
que quatre hommes. Tous les autres ont été tués par des disques
d'acier. Vous ne pouvez vous arrêter très longtemps car l'ennemi
s'est peut-être déjà lancé à votre poursuite. Vous repartez donc
vers le sud, le long de la grande route, en compagnie de vos
patrouilleurs rescapés. Et, tandis que vous chevauchez, le
sifflement terrifiant des disques mortels résonne encore à vos
oreilles, tel un écho lointain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_297.py", label="297", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
