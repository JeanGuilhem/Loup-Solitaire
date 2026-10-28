import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=108, book=3)

fr_text = """
Vous voyez passer la patrouille devant vous et vous attendez que
le bruit de pas se soit éloigné pour monter l'escalier. Mais
soudain, un cri retentit, vous faites volte-face et vous apercevez
la silhouette d'un Barbare des Glaces qui vient d'apparaître dans
l'obscurité. Il se précipite sur vous en brandissant une lance à la
pointe d'os.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.caption("Vous avez le droit de fuir après le premier Assaut en montant l'escalier quatre à quatre.")
    outcome = combat([("BARBARE DES GLACES", 16, 24)], flee_after=1)
    if outcome == "fled":
        st.write_stream(stream_text("Si vous souhaitez prendre à droite la direction du sud, rendez-vous au :"))
        st.page_link("tomes/tome3/page_330.py", label="330", icon="📄")
        st.write_stream(stream_text("Si vous préférez prendre la fuite en allant à gauche, en direction du nord, rendez-vous au :"))
        st.page_link("tomes/tome3/page_198.py", label="198", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous combattez jusqu'au bout et que vous sortez vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome3/page_282.py", label="282", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
