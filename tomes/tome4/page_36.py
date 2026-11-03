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

check_inventory(current_page_number=36, book=4)

fr_text = """
Les Chiens de Guerre se précipitent dans votre direction à une
vitesse décourageante. Vous distinguez nettement leurs énormes
mâchoires aux babines rouges et vous entendez leurs crocs
s'entrechoquer. Vous vous efforcez de contrôler votre respiration
et vous faites appel à toutes vos ressources d'habile guerrier : il
vous faut en effet vous débarrasser de ces Chiens de Guerre sans
commettre la moindre erreur, sinon vous serez littéralement
déchiqueté. Deux molosses plus rapides que leurs congénères se
détachent de la meute et se ruent sur vous. Ils bondissent en
même temps, leurs mâchoires grandes ouvertes dégoulinant de
bave. Vous plongez à terre et vous roulez sur vous-même en les
frappant au ventre à l'instant précis où ils s'élancent au-dessus
de vous. Les deux créatures poussent un hurlement de rage et de
douleur puis s'effondrent sans vie sur le sol. Vous vous relevez
aussitôt, juste à temps pour affronter un nouveau Chien de
Guerre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("CHIEN DE GUERRE", 17, 25)])
    if outcome == "win":
        if st.session_state["combat_combat"]["round"] <= 3:
            st.write_stream(stream_text("Vous avez gagné le combat en 3 Assauts ou moins, rendez-vous au :"))
            st.page_link("tomes/tome4/page_155.py", label="155", icon="📄")

        else:
            st.write_stream(stream_text("Il vous a fallu plus de 3 Assauts pour remporter la victoire, rendez-vous au :"))
            st.page_link("tomes/tome4/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
