import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=50, book=4)

fr_text = """
Les grandes portes s'ouvrent pour livrer passage à une patrouille
de six Gardes des Tunnels. Chacun d'eux est armé d'une arbalète.
En vous voyant sur le pont, ils réagissent instantanément.
« Chargez ! » Vous venez de lancer cet ordre en espérant que vos
hommes pourront maîtriser les Gardes avant qu'ils n'aient le
temps d'actionner leurs armes mortelles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez un chiffre entre 0 et 6, rendez-vous au 184. Si vous tirez le 7, le 8 ou le 9, rendez-vous au 267."))
    number = hazard_roll()
    if number is not None and number <= 6:
        st.page_link("tomes/tome4/page_184.py", label="184", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome4/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
