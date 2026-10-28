import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=55, book=3)

fr_text = """
Vous êtes à moins de 30 mètres du sommet lorsque vos mains
cessent peu à peu de vous faire mal. Bientôt, vous ne sentez plus
rien du tout : le gel vous a rendu insensible des avant-bras à
l'extrémité des doigts. Dans un dernier effort, vous atteignez un
étroit rebord de glace sur lequel vous pouvez vous agenouiller et
vous reposer un peu. Quelques instants plus tard, cependant,
vous vous rendez compte qu'il vous est impossible de grimper
plus haut. En effet, vous vous trouvez face à des parois de glace
abruptes dont la surface lisse n'offre aucune prise. Il vous faut
donc redescendre. Vous ne retrouvez la sensibilité de vos mains
que plus de quatre heures après, et la morsure du gel vous fait
perdre 5 points d'ENDURANCE. En outre, vous perdez
également 2 points d'HABILETÉ à déduire de votre total de
départ. Cette perte est définitive et durera jusqu'à la fin de votre
vie. Cinq heures vous sont nécessaires pour revenir au pied de la
montagne. Epuisé et rongé par la douleur, vous vous armez de
courage pour essayer de trouver un autre moyen d'échapper à ce
gouffre infernal.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.session_state.hability -= 2  # perte définitive
        change_endurance(-5)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-5)
    st.metric(label="Habileté", value=st.session_state.hability, delta=-2)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_182.py", label="182", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
