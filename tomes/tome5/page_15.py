import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=15, book=5)

fr_text = """
Le tunnel est plongé dans l'obscurité. Il est en grande partie
délabré et ses parois sont lézardées par de multiples fissures.
Vous devez essayer de trouver une anfractuosité qui soit assez
large pour vous dissimuler.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez le titre de Gardien Kaï, ou un titre supérieur, déduisez 1 point du chiffre que vous avez tiré.'))
    roll = hazard_roll()
    if roll is not None:
        malus = 1 if kai_rank() >= 7 else 0
        total = roll - malus
        if malus:
            st.write(f"*Malus : -{malus}, soit un total de {total}.*")
        if total <= 7:
            st.write_stream(stream_text('Si le résultat est compris entre -1 et 7, rendez-vous au :'))
            st.page_link("tomes/tome5/page_151.py", label="151", icon="📄")
        else:
            st.write_stream(stream_text('Si le résultat est compris entre 8 et 9, rendez-vous au :'))
            st.page_link("tomes/tome5/page_175.py", label="175", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
