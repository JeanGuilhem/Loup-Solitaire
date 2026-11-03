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

check_inventory(current_page_number=32, book=4)

fr_text = """
La hideuse créature vous lâche les jambes et sombre au fond de
l'eau. Votre victoire vous réjouit, mais vous avez l'impression que
vos poumons sont en feu. Vous vous débattez pour remonter à la
surface et vous parvenez enfin à respirer à nouveau, toussant et
haletant. Il ne reste du bateau et de vos hommes qu'une rame
fracassée qui flotte à la surface de la sombre et terrifiante rivière.
Vous vous accrochez à ce débris et vous vous laissez emporter
par le courant en direction de la rive opposée sur laquelle vous
vous hissez. En vérifiant le contenu de votre Sac à Dos et de vos
poches, vous constatez que vous n'avez rien perdu au cours de
votre lutte dans l'eau, mais c'est là une mince consolation au
regard de la catastrophe que représente la mort de vos hommes.
Vous refusez cependant de perdre courage et vous décidez de
poursuivre votre chemin vers Ruanon pour tenter de percer le
mystère qui pèse sur la province.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Avant d'entrer dans le tunnel orienté à l'est, vous jetez un dernier regard à la rivière aux eaux noires puis vous vous rendez au :"))
    st.page_link("tomes/tome4/page_309.py", label="309", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
