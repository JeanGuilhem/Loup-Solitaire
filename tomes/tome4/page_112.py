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

check_inventory(current_page_number=112, book=4)

fr_text = """
Le pont s'écrase contre la paroi rocheuse dans un grand fracas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si votre total actuel d'ENDURANCE est inférieur à 10, vous devrez déduire 3 points du chiffre que vous aurez tiré. Si, en revanche, votre total actuel d'ENDURANCE est supérieur à 20, vous ajouterez 3 points au chiffre donné par la Table."))
    roll = hazard_roll()
    if roll is not None:
        if st.session_state.endurance < 10:
            bonus = -3
        elif st.session_state.endurance > 20:
            bonus = 3
        else:
            bonus = 0
        total = roll + bonus
        if bonus:
            st.write(f"*ENDURANCE actuelle : {st.session_state.endurance}, {bonus:+d}, soit un total de {total}.*")
        if total <= 4:
            st.write_stream(stream_text('Si le total obtenu est de 3 à 4, rendez-vous au :'))
            st.page_link("tomes/tome4/page_42.py", label="42", icon="📄")
        else:
            st.write_stream(stream_text('De 5 à 12, rendez-vous au :'))
            st.page_link("tomes/tome4/page_303.py", label="303", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
