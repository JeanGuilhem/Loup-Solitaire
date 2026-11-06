import streamlit as st
from inventory import (
    check_inventory,
    choose_item_to_lose,
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

check_inventory(current_page_number=166, book=6)

fr_text = """
Votre cheval essaie vaillamment de sauter par-dessus le chariot,
mais la longue course de la journée lui a coupé toute sa fougue.
Ses jambes avant heurtent les montants du véhicule, et vous êtes
soudainement projeté en avant de votre selle. Vous tirez
désespérément sur les rênes afin de maîtriser l'animal affolé, qui
piétine frénétiquement le chargement avant d'atterrir, dans un
terrible fracas, sur le pavé de la rue. Fort heureusement, vous
parvenez à reprendre le contrôle de la situation et à aiguillonner
votre monture vers la rue tortueuse qui part de la place. Vous ne
vous arrêtez que lorsque les cris des gardes et les injures des
marchands se sont enfin évanouis loin derrière vous. Mettant
pied à terre, vous caressez longuement l'encolure et les flancs de
votre vaillante monture pour la rassurer, puis vous examinez ses
blessures. Ses jambes avant sont couvertes d'ecchymoses mais la
peau n'est pas entaillée. Après une bonne nuit de repos, il n'y
paraîtra plus. Alors que vous remontez en selle, vous découvrez
avec consternation que le rabat de votre Sac à Dos s'est ouvert.
Après en avoir rapidement inspecté le contenu, vous constatez
qu'il vous manque 2 Objets.
Vous les avez sans doute perdus en sautant l'obstacle. Rayez au
choix 2 Objets sur votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # rayez au choix 2 Objets du Sac à Dos (le rabat s'est ouvert)
    first = choose_item_to_lose(list(dict.fromkeys(st.session_state.backpack)), key="t6_166_1",
                                label="Choisissez le premier Objet perdu :")
    second = first and choose_item_to_lose(list(dict.fromkeys(st.session_state.backpack)), key="t6_166_2",
                                           label="Choisissez le second Objet perdu :")
    if second:
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("tomes/tome6/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
