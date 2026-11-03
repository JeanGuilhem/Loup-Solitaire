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

check_inventory(current_page_number=65, book=4)

fr_text = """
Lorsque vous marchez dessus, les champignons roses éclatent en
laissant échapper des nuages de spores dans le tunnel. Les spores
vous piquent les yeux et vous empêchent de respirer. Vous
continuez d'avancer à l'aveuglette d'un pas chancelant, mais à
peine avez-vous émergé de ce nuage qu'un autre danger vous
menace. Une nuée de reptiles hideux dotés d'ailes de chauve-souris
volent dans votre direction. Leurs pattes couvertes
d'écailles enserrent des morceaux pointus de stalagmites. Il vous
est impossible d'échapper au combat et vous devrez affronter ces
créatures en les considérant comme un seul et même ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DÉMONS DES SOUTERRAINS", 20, 10)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome4/page_298.py", label="298", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
