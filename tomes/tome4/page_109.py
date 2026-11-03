import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=109, book=4)

fr_text = """
D'un coup de pied vous retournez le cadavre du bandit puis vous
le fouillez. Vous découvrez alors les objets suivants :
- 3 Pièces d'Or,
- 1 Poignard,
- 1 Épée,
Vous pouvez prendre l'un ou l'autre de ces objets, en n'oubliant
pas de les inscrire sur votre Feuille d'Aventure. Vous vous
apprêtez à repartir, lorsque vous remarquez une trappe dans le
plancher. En l'ouvrant, vous découvrez un escalier qui descend
dans la cave de la cabane.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(3, key="gold")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")

    st.write_stream(stream_text('Si vous souhaitez fouiller la cave, rendez-vous au :'))
    st.page_link("tomes/tome4/page_347.py", label="347", icon="📄")

    st.write_stream(stream_text('Si vous préférez quitter la cabane, rendez-vous au :'))
    st.page_link("tomes/tome4/page_258.py", label="258", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
