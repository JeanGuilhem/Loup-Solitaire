import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=348, book=2)

fr_text = """
L'homme cesse de sourire et une expression de mépris apparaît sur son
visage. D'un mouvement rapide, il s'éloigne de la table. « Peut-être que
ni vous ni moi ne sommes celui que nous prétendons être, mais
qu'importe, vous ne vivrez pas assez longtemps pour découvrir qui je
suis ! » lance-t-il avec hargne. Vous entendez alors une porte s'ouvrir à
la volée derrière vous. Vous faites aussitôt volte-face et vous voyez
trois BRIGANDS s'avancer dans votre direction. Chacun d'eux est armé
d'un cimeterre et vous allez devoir les combattre en les considérant
comme un seul et même adversaire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous aurez le droit de prendre la fuite après avoir mené contre eux deux assauts au moins."))
    outcome = combat([("BRIGANDS", 16, 25)], flee_after=2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome2/page_333.py", label="333", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous sortez par la porte latérale, rendez-vous au :"))
        st.page_link("tomes/tome2/page_125.py", label="125", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
