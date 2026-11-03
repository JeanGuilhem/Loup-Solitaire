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

check_inventory(current_page_number=81, book=4)

fr_text = """
Les cris rauques du Garde retentissent dans le tunnel. Vous
parvenez bientôt à une bifurcation où des travaux sont en cours.
Au milieu du tunnel, un étai soutient une poutre affaissée. Si
vous réussissiez à dégager cet étai, vous pourriez provoquer un
éboulement qui bloquerait le passage derrière vous. Vous
entendez à présent des bruits de pas précipités vous indiquant
que plusieurs Gardes courent dans votre direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez essayer d'abattre l'étai, rendez-vous au :"))
    st.page_link("tomes/tome4/page_173.py", label="173", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous en abstenir et continuer à fuir le long du tunnel, rendez-vous au :"))
    st.page_link("tomes/tome4/page_224.py", label="224", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
