import streamlit as st
from combat import combat_weapons
from inventory import (
    change_endurance,
    check_inventory,
    choose_item_to_lose,
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

check_inventory(current_page_number=18, book=3)

fr_text = """
Lorsque votre épée s'enfonce dans le vent tourbillonnant, une
soudaine douleur provoquée par un froid intense vous parcourt
le bras. Vous perdez 3 points d'ENDURANCE et vous reculez
d'un pas chancelant en tenant votre bras meurtri par le froid
contre votre poitrine. Vous avez perdu votre arme et le cyclone
devient de plus en plus puissant, vous forçant à vous réfugier
dans un coin du temple.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    # l'arme qui a frappé le cyclone est perdue : le joueur indique celle qu'il tenait
    if choose_item_to_lose(combat_weapons(), key="arme_perdue", label="Quelle arme teniez-vous ?"):
        st.write_stream(
            stream_text(
                "Si vous souhaitez essayer de vous enfuir vers l'arcade qui se trouve au-delà du "
                'tourbillon, rendez-vous au :'
            )
        )
        st.page_link("tomes/tome3/page_211.py", label="211", icon="📄")

        st.write_stream(
            stream_text(
                "Si vous préférez rester dans le coin du temple en espérant que vous y serez à l'abri, "
                'rendez-vous au :'
            )
        )
        st.page_link("tomes/tome3/page_95.py", label="95", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
