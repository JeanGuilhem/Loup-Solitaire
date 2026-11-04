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

check_inventory(current_page_number=213, book=5)

fr_text = """
Le Drakkar tombe à genoux et vous entendez d'horribles
grincements métalliques tandis qu'il essaie, en vain, d'arracher
son masque à tête de mort. Son heaume a, dans un premier
temps, amorti vos coups mais ensuite le métal s'est enfoncé et lui
a fracturé le crâne. Vous lui donnez un violent coup de pied qui
l'envoie basculer par-dessus bord. Son corps tombe en
tournoyant vers le lac Inrahim où il va rejoindre le Nain qu'il
vient de tuer. Tout à coup, vous apercevez une jambe retenue
prisonnière dans les cordages du bastingage : le Nain n'est pas
mort et encore moins en compagnie du Drakkar, plusieurs
dizaines de mètres plus bas ! Il est là, accroché aux cordages ;
vous le saisissez par la jambe et vous le hissez à bord avant de
reprendre le combat. La plate-forme a l'air déserte ; aucune tête
ne dépasse du parapet blindé, mais vous sentez qu'il se passe
quelque chose d'anormal. Instinctivement, vous sautez du pont
arrière, et vous vous dirigez vers la plate-forme en brandissant
votre arme, prêt à frapper.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_361.py", label="361", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
