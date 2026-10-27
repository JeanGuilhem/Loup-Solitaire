import streamlit as st
from combat import combat
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

check_inventory(current_page_number=268, book=2)

fr_text = """
«Vous êtes sans nul doute un Seigneur Kaï», dit l'homme, mais
l'expression stupéfaite de son visage se transforme bientôt en un
ricanement méprisant. « Ou plutôt, reprend-il d'une voix ironique, vous
étiez un Seigneur Kaï ! » A peine a-t-il prononcé ces mots qu'une porte
s'ouvre à la volée juste derrière vous. Vous faites volte-face et vous
vous retrouvez face à trois BRIGANDS qui s'avancent dans votre
direction. Chacun d'eux est armé d'un cimeterre et vous devez les
combattre en les considérant comme un seul et même ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Vous aurez le droit de prendre la fuite après avoir mené deux assauts ; vous sortirez alors par la porte latérale en vous rendant au 125. Si vous êtes vainqueur, rendez-vous au 333.'))
    outcome = combat([("BRIGANDS", 16, 25)], flee_after=2)
    if outcome == "win":
        st.page_link("tomes/tome2/page_333.py", label="333", icon="📄")
    elif outcome == "fled":
        st.page_link("tomes/tome2/page_125.py", label="125", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
