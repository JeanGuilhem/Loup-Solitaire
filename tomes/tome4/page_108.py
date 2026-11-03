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

check_inventory(current_page_number=108, book=4)

fr_text = """
Le chef des Gardes des Tunnels lance un ordre à ses hommes, qui
s'immobilisent aussitôt. De toute évidence, il vient de leur
ordonner de ne pas se mêler d'un combat qu'il se réserve pour
lui-même. L'officier porte un grand heaume empanaché ainsi
qu'une écharpe d'un rouge vif en travers de la poitrine. D'un bref
mouvement, il pointe sa hallebarde en direction de votre tête et
passe à l'attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("OFFICIER DES GARDES", 20, 30)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous pouvez prendre la fuite à tout moment en vous précipitant de l'autre côté du pont. Rendez-vous pour cela au :"))
        st.page_link("tomes/tome4/page_271.py", label="271", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text('Si vous sortez vainqueur du combat, rendez-vous au :'))
        st.page_link("tomes/tome4/page_28.py", label="28", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
