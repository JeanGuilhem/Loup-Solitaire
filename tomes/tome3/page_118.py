import streamlit as st
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

check_inventory(current_page_number=118, book=3)

fr_text = """
Le vieil homme est beaucoup trop faible pour grimper tout seul.
Vous lui conseillez alors d'attacher la Corde autour de sa taille
pour que vous puissiez ainsi le hisser hors de sa prison. Avec des
gestes lents, il suit vos instructions et, lorsqu'il est enfin prêt,
vous avez la surprise de constater, en le soulevant, qu'il ne pèse
pas plus lourd qu'un enfant. Quelques minutes plus tard, vous
avez réussi à le tirer hors de son cachot et il se retrouve en face
de vous, dans le couloir. Il vous faut à présent découvrir qui il
est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_56.py", label="56", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
