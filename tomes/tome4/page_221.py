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

check_inventory(current_page_number=221, book=4)

fr_text = """
Vous arrivez bientôt dans une salle séparée en deux par un large
gouffre. Il règne ici un silence mortel et le moindre bruit résonne
en écho contre les murs de pierre grise, comme un éclat de
cymbales. Un pont en maçonnerie enjambe le gouffre et mène à
deux portes massives également en pierre. Vous vous engagez
sur le pont et, quelques instants plus tard, vous entendez un
grondement assourdissant. Les portes sont en train de s'ouvrir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez dégainer votre arme et vous préparer à combattre, rendez-vous au :'))
    st.page_link("tomes/tome4/page_50.py", label="50", icon="📄")

    st.write_stream(stream_text("Si vous préférez fuir ce pont, rebrousser chemin le long du tunnel et descendre l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome4/page_228.py", label="228", icon="📄")

    st.write_stream(stream_text('Enfin, si vous voulez prendre le risque de sauter par-dessus le parapet du pont, dans les profondeurs inconnues du gouffre, rendez-vous au :'))
    st.page_link("tomes/tome4/page_342.py", label="342", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
