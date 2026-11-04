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

check_inventory(current_page_number=384, book=5)

fr_text = """
Malheureusement, vous avez mal apprécié la distance qui vous
séparait de votre cible. Vous n'avez pas lancé la Flèche de
Sommeil assez fort et celle-ci atteint une mouette qui s'était
posée sur la plate-forme d'atterrissage. Le malheureux oiseau fait
quelques pas en titubant puis tombe sur le dos, ses pattes raidies
pointées vers le ciel. Le Garde s'avance vers l'oiseau puis, d'un
coup de pied, l'envoie négligemment basculer par-dessus le
rebord de la plate-forme. Il le regarde ensuite tournoyer vers les
jardins en contrebas, sans se douter qu'il vient d'éviter lui-même
une fin identique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_282.py", label="282", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
