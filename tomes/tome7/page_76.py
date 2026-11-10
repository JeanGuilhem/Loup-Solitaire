import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=76, book=7)

fr_text = """
Dans sa rage de ne pas pouvoir vous faire lâcher prise, le Lekhor
se contorsionne en tous sens. Il rejette la tête en arrière, et une
goutte de venin tombe sur le dessus de votre main. Cela vous
brûle comme un coup de poignard chauffé à blanc et vous ne
pouvez réprimer un cri de douleur. Le serpent siffle
bruyamment, sa longue langue fourchue fouettant furieusement
l'air en passant à quelques centimètres de votre visage.
En raison de votre position précaire, vous ne pouvez pas vous
servir de votre bouclier durant le combat. Par ailleurs, à cause du
venin terriblement corrosif du Lekhor, vous devrez tripler tous
les Points d'ENDURANCE que vous perdrez éventuellement lors
de l'affrontement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # pas de Bouclier pendant ce combat : on retire les +2 que le moteur lui accorde
    # venin : vos pertes d'ENDURANCE sont triplées
    outcome = combat([("LEKHOR", 16, 30)], hability_modifier=-2 if has_item("BOUCLIER") else 0, ls_loss_multiplier=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de ce combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_296.py", label="296", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
