import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=321, book=2)

fr_text = """
Le repas frugal est composé de restes de la veille qui n'ont rien
d'appétissant. A la fin de ce piètre souper, le capitaine vous fait
quelques confidences qui confirment vos craintes. « Je dois vous
avouer quelque chose, Seigneur Kaï, dit-il : le feu a détruit tous nos
vivres et il ne restait plus dans la cambuse que de quoi préparer ce
maigre repas. D'ici à Port Bax, il faudra nous contenter du poisson que
nous pourrons pêcher... » A moins qu'il ne vous reste de quoi manger
dans votre Sac à Dos, ce détestable dîner vous laisse sur votre faim et
vous perdez 2 points d'ENDURANCE. Plus tard dans la soirée, le
capitaine vous propose une partie de Samor ; c'est un jeu semblable aux
échecs qui demande beaucoup d'ingéniosité et d'audace. Pour ajouter à
l'intérêt de la partie, le capitaine vous invite à miser un peu d'or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas(penalty=2, hunting=False)

    st.write_stream(stream_text("Si vous acceptez son offre, rendez-vous au :"))
    st.page_link("tomes/tome2/page_12.py", label="12", icon="📄")
    st.write_stream(stream_text("Si en revanche vous n'avez pas envie de jouer, souhaitez une bonne nuit au capitaine et rentrez dormir dans votre cabine en vous rendant au :"))
    st.page_link("tomes/tome2/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
