import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=301, book=5)

fr_text = """
Utilisant les barres de fer comme les barreaux d'une échelle, vous
escaladez la porte dont le haut est hérissé de longues piques en
bois enduites d'une sorte de goudron huileux. Au moment précis
où vous enjambez précautionneusement l'obstacle, les Gardes
tirent sur vous à l'aide de leurs arbalètes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez le titre de Gardien Kaï (ou un titre supérieur), déduisez 2 points du chiffre que vous avez tiré. Si vous maîtrisez la Discipline Kaï de la Chasse, déduisez 1 point de ce même chiffre.'))
    roll = hazard_roll()
    if roll is not None:
        malus = 0
        if kai_rank() >= 7:
            malus += 2
        if has_kai("La Chasse"):
            malus += 1
        total = roll - malus
        if malus:
            st.write(f"*Malus : -{malus}, soit un total de {total}.*")
        if total < 4:
            st.write_stream(stream_text('Si le résultat obtenu est inférieur à 4, rendez-vous au :'))
            st.page_link("tomes/tome5/page_363.py", label="363", icon="📄")
        else:
            st.write_stream(stream_text('Si le résultat obtenu est compris entre 5 et 9, rendez-vous au :'))
            st.page_link("tomes/tome5/page_259.py", label="259", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
