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

check_inventory(current_page_number=48, book=7)

fr_text = """
A peine avez-vous parcouru une centaine de mètres qu'un cri
lugubre retentit derrière vous. En vous retournant, vous
apercevez la silhouette d'un gigantesque loup noir qui fonce sur
vous à une vitesse terrifiante. Ses yeux brillent dans la pénombre,
et sa gueule grande ouverte, prête à vous happer, découvre de
puissants crocs recourbés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez vous préparer à combattre ce féroce animal, rendez-vous au :'))
    st.page_link("tomes/tome7/page_78.py", label="78", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous enfuir à toutes jambes, rendez-vous au :'))
    st.page_link("tomes/tome7/page_287.py", label="287", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
