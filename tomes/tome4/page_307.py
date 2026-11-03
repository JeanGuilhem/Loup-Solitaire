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

check_inventory(current_page_number=307, book=4)

fr_text = """
Des groupes de brigands sortent de la forêt, fouettés par des
sergents furieux qu'ils vous aient laissé échapper. Cette vision
vous incite à hâter le pas. Vous parcourez les cent premiers
mètres sans difficulté. C'est alors que des flèches commencent à
tomber autour de vous. Vous vous baissez aussitôt et vous courez
en zigzag, constituant ainsi une cible difficile à atteindre. Peu à
peu, le nombre de flèches diminue sans que vous ayez été touché
une seule fois. Les vains efforts des archers vous font sourire,
mais votre confiance en vous-même est bientôt ébranlée par un
nouveau péril : une meute de Chiens de Guerre vient en effet de
surgir de la forêt à votre droite. De toute évidence, ils sont
assoiffés de sang et personne n'est là pour les retenir. Vous êtes à
moins de 500 mètres de Ruanon, mais les molosses se
rapprochent à une allure inquiétante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez essayer de courir plus vite dans l'espoir de les distancer, rendez-vous au :"))
    st.page_link("tomes/tome4/page_225.py", label="225", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous arrêter et les combattre, rendez-vous au :"))
    st.page_link("tomes/tome4/page_36.py", label="36", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
