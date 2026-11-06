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

check_inventory(current_page_number=282, book=6)

fr_text = """
D'un mouvement souple et rapide, vous esquivez le poignard et
dégainez votre arme. La lame du couteau vous égratigne le flanc,
mais vous avez réussi à éviter une blessure grave. Les deux hommes
ricanent méchamment et s'avancent, prêts au combat. Vous n'avez
aucune possibilité de fuite et vous devez les affronter comme s'il
s'agissait d'un seul et même ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BRIGANDS AU COUTEAU", 18, 25)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome6/page_88.py", label="88", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
