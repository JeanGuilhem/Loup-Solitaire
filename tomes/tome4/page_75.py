import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=75, book=4)

fr_text = """
A peine le Guerrier s'est-il effondré sur le sol qu'un autre vous
attaque par le flanc. Au moment où vous vous tournez pour lui
faire face, la pointe de sa lance vous atteint au bras gauche et
vous perdez 2 points d'ENDURANCE. Vous vous recroquevillez
sous l'effet de la douleur puis, poussé par d'autres combattants,
vous glissez et vous tombez sur le sol déjà couvert de cadavres.
Vous apercevez alors une porte ouverte et vous rampez dans
cette direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Camouflage, ajoutez 3 au chiffre que vous aurez tiré."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (3 if has_kai("Le Camouflage") else 0)
        if has_kai("Le Camouflage"):
            st.write(f"*Camouflage : +3, soit un total de {total}.*")
        if total <= 5:
            st.write_stream(stream_text("Si vous obtenez un total de 0 à 5, rendez-vous au :"))
            st.page_link("tomes/tome4/page_192.py", label="192", icon="📄")
        else:
            st.write_stream(stream_text("De 6 à 12, rendez-vous au :"))
            st.page_link("tomes/tome4/page_16.py", label="16", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
