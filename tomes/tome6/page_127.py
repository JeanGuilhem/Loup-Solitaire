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

check_inventory(current_page_number=127, book=6)

fr_text = """
La porte se referme sur vous avec un claquement sec. Il vous
faut quelques secondes pour habituer vos yeux à la pénombre de
l'endroit, mais vous constatez bientôt que vous vous trouvez
probablement dans l'antichambre d'une vaste salle. Vous
orientant d'après les chuchotements que vous percevez, vous vous
engagez sous une porte voûtée, puis vous suivez le couloir
menant à la pièce principale. Là, vous découvrez, réunis autour
d'une grande table ronde en métal brillant, plusieurs
vieillards, penchés au-dessus de livres et de cartes
astronomiques. Ils sont engagés dans une conversation animée.
Pour éclairer leur travail, des globes immobiles, suspendus en
l'air au-dessus de leurs têtes, diffusent une lumière bleutée.
Personne n'a remarqué votre présence. Mais, alors que vous vous
approchez de la table d'acier, la réaction des vieux érudits en
vous apercevant soudain est étonnante : ils vous regardent tous
comme si vous étiez un revenant ; certains se mettent à pousser
des cris, la stupeur la plus totale se lit dans leurs yeux
écarquillés, et des gouttes de sueur commencent à perler sur
leur front. Votre apparition cause un choc si violent à l'un des
vieillards qu'il en défaille, s'affalant mollement sur les
cartes et les livres qui jonchent la table. De toute
l'assemblée, seul un homme parvient à conserver son calme et son
sang-froid.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # visite d'un tome précédent non mémorisée par l'application : le joueur choisit lui-même
    st.write_stream(stream_text("S'il vous est déjà arrivé de visiter une cabane sur la Route des Brigands, lors d'une précédente aventure de la série Loup Solitaire, rendez-vous au :"))
    st.page_link("tomes/tome6/page_233.py", label="233", icon="📄")

    st.write_stream(stream_text("Si vous n'êtes jamais allé dans un tel endroit, rendez-vous au :"))
    st.page_link("tomes/tome6/page_6.py", label="6", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
