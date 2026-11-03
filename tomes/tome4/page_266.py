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

check_inventory(current_page_number=266, book=4)

fr_text = """
« Il y a presque un mois que nous n'avons plus de nouvelles, dit-
il en hochant sa tête barbue. Quelques cavaliers de votre pays
sont passés par ici à cette époque mais, depuis, nous n'avons vu
personne d'autre, à part une troupe de troubadours en
provenance de Clœasia et, bien entendu, ces maudits brigands. »
Les trois jeunes gens, qui se révèlent être les fils du tenancier,
décident de prendre des tours de garde derrière les meurtrières
aménagées dans les murs ; vos hommes et vous pourrez ainsi
dormir quelques heures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_324.py", label="324", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
