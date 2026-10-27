import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=289, book=2)

fr_text = """
Vous êtes accueilli par une vieille femme vêtue de blanc des pieds à la
tête. Elle vous sourit et vous offre une tasse de délicieux Jala. Mais les
mésaventures que vous avez vécues à Ragadorn vous ont rendu méfiant
et vous refusez poliment de boire le liquide sombre contenu dans la
tasse qu'elle vous tend. Vous avez fait un geste de la main pour décliner
son offre et elle a vu alors le Sceau d'Hammardal passé à votre doigt. «
Quelle bague magnifique ! Est-elle à vendre ? » demande-t-elle le
regard brillant de convoitise. Vous lui répliquez d'un ton ferme qu'il
n'en est rien mais elle ne se contente pas de cette réponse. Elle vous
propose, en échange de l'anneau, l'une des centaines de potions qui
remplissent les vitrines alignées derrière le comptoir. Vous haussez les
épaules sans même prendre la peine de répondre et vous vous tournez
vers la porte avec la ferme intention de quitter aussitôt la boutique. A
ce moment, elle vous offre 40 Pièces d'Or pour prix de l'anneau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Allez-vous cette fois accepter le marché ? Rendez-vous dans ce cas au :'))
    st.page_link("tomes/tome2/page_165.py", label="165", icon="📄")

    st.write_stream(stream_text("Si cette proposition ne vous fait pas changer d'avis, sortez de la boutique et rendez-vous au :"))
    st.page_link("tomes/tome2/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
