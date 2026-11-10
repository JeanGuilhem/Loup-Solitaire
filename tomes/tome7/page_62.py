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

check_inventory(current_page_number=62, book=7)

fr_text = """
Le garde tire tandis que vous courez vers lui. D'après le mauvais
sourire qui s'affiche sur ses lèvres, il est évident que, pour lui,
vous serez bientôt un homme mort ! Au risque de le décevoir,
vous faites un brusque écart pour éviter le projectile meurtrier, et
le carreau ne fait que déchirer votre manche. Décontenancé par
son échec, le garde tente de parer votre attaque à l'aide de son
arbalète, mais vous la lui arrachez rapidement des mains et il se
retrouve désarmé et tremblant face à vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE DE LA SALLE DU TRÔNE", 14, 22)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de ce combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_282.py", label="282", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
