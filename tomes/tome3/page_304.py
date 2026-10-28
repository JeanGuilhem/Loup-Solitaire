import streamlit as st
from combat import combat
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

check_inventory(current_page_number=304, book=3)

fr_text = """
Le Glaive puissant illumine le passage de son flamboiement d'or.
Le Monstre d'Enfer pousse un hurlement aigu et bat en retraite,
les yeux rouges étincelant de haine et de peur. Il a reconnu en
effet l'arme que vous brandissez, une arme dont le pouvoir
signifie, pour ceux de son espèce, la mort et la destruction
éternelle. Saisi de panique, il vous attaque en faisant usage de sa
redoutable Puissance Psychique. Si vous ne maîtrisez pas la
Discipline Kaï du Bouclier Psychique, vous perdrez 2 points
d'ENDURANCE supplémentaires à chaque Assaut que vous
livrerez contre cette créature. Sachez aussi qu'elle est elle-même
invulnérable à votre propre Puissance Psychique, si vous
maîtrisez cette Discipline Kaï. Cependant, le Monstre d'Enfer
appartenant à l'espèce des morts vivants, vous aurez le droit de
doubler tous les points d'ENDURANCE perdus par lui, cela en
raison de la puissance du Glaive de Sommer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("MONSTRE D'ENFER", 22, 30)], psychic_immune=True, psychic_damage=2, undead=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez la victoire, rendez-vous au :"))
        st.page_link("tomes/tome3/page_20.py", label="20", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
