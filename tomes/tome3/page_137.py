import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=137, book=3)

fr_text = """
La porte s'ouvre en grinçant et vous la franchissez, prêt à
l'attaque. Vous parvenez à tuer deux des créatures endormies
avant que les Barbares des Glaces et le troisième Loup Maudit
n'aient eu le temps de réagir. Ils bondissent alors sur vous d'un
même élan et il vous faut les combattre en les considérant
comme un seul et même adversaire. Ils sont partiellement
insensibles à la Puissance Psychique, et si vous maîtrisez cette
Discipline Kaï, vous n'aurez le droit d'ajouter qu'un seul point à
votre total d'HABILETÉ pendant toute la durée de ce combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # partiellement insensibles : la Puissance Psychique ne donne que +1 au lieu de +2
    outcome = combat(
        [("BARBARE DES GLACES ET LOUP MAUDIT", 30, 30)],
        psychic_immune=True,
        hability_modifier=1 if has_kai("Puissance psychique") else 0,
    )
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome3/page_28.py", label="28", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
