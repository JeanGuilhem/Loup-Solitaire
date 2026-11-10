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

check_inventory(current_page_number=93, book=7)

fr_text = """
Se frayer un chemin à travers les toiles d'araignée est un exercice
plus ardu que prévu et vous vous retrouvez peu à peu couvert des
pieds à la tête de fils solides et poisseux. Une indicible angoisse
vous étreint lorsque vous réalisez qu'ils commencent à se
resserrer ! Il vous faut réagir sans perdre une seconde - c'est une
question de vie ou de mort. L'ignoble substance animée qui vous
a pris au piège est insensible à la Puissance Psychique, tout
comme au Foudroiement Psychique. En raison de votre faible
capacité de mouvement, réduisez votre total d'HABILETÉ de 4
points pour toute la durée du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("TOILE-PIÈGE", 14, 34)], psychic_immune=True, hability_modifier=-4)
    if outcome == "win":
        st.write_stream(stream_text("Si vous l'emportez, rendez-vous au :"))
        st.page_link("tomes/tome7/page_131.py", label="131", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
