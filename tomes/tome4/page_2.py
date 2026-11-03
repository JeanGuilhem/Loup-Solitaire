import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=2, book=4)

fr_text = """
En fouillant les cadavres des brigands, vous découvrez les objets
suivants :
- 1 Épée,
- 1 Masse d'Armes,
- 1 Poignard,
- 1 Marteau de Guerre,
- 12 Pièces d'Or,
- 1 Sac à Dos,
- des vivres équivalants à 2 Repas.
Vous pouvez prendre un ou plusieurs de ces objets en n'oubliant
pas de les noter sur votre Feuille d'Aventure. Vous ramassez
ensuite la carte posée sur la table tachée de sang et vous
remarquez alors que la pièce dans laquelle vous vous trouvez a
été entourée à l'encre noire. Ce plan vous indique qu'une porte
aménagée dans le mur du fond ouvre sur une galerie qui mène
directement à la surface. Impatient de quitter ce lieu où règne la
mort, vous franchissez la porte et vous courez le long du passage
en direction d'un lointain rayon de soleil. Il vous faut plusieurs
secondes pour habituer vos yeux à la lumière du jour, mais peu à
peu vous réalisez enfin que vous avez réussi à vous échapper des
mines de Maaken ; vous êtes à présent dans les contreforts de
l'est à moins de 3 kilomètres de la ville de Ruanon elle-même.
Vous apercevez cependant un groupe de Guerriers Pillards qui
inspectent l'une des entrées de la mine, juste au-dessous de la
corniche rocheuse sur laquelle vous êtes à présent accroupi. Si
vous voulez atteindre Ruanon vivant, vous devez à tout prix
éviter ces brigands. Vous attendez donc que le groupe de Pillards
soit hors de vue puis vous descendez un sentier escarpé qui mène
à une forêt touffue. Vous faites une brève halte pour reprendre
votre souffle et vous repartez aussitôt après en direction de
Ruanon que vous atteindrez après avoir traversé la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not st.session_state.has_backpack:
        pickup_button("SAC À DOS", key="sac", label="Prendre le Sac à Dos")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("MASSE D'ARMES", key="masse", label="Prendre la Masse d'Armes")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
    pickup_button("MARTEAU DE GUERRE", key="marteau", label="Prendre le Marteau de Guerre")
    pickup_gold(12, key="gold")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_2", label="Prendre 1 Repas")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
