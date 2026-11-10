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

check_inventory(current_page_number=39, book=7)

fr_text = """
Vous avez le pressentiment qu'un pont, dissimulé à vos regards
par un sortilège d'invisibilité, enjambe le gouffre. Vous vous
agenouillez au bord du vide, puis vous promenez vos mains le
long du rebord afin de repérer le pont, mais vous entendez
soudain du bruit et vous faites rapidement volte-face. Un bruit de
pas lourds est en train de se rapprocher, mais vous n'apercevez
rien dans le passage. Saisi d'une indicible angoisse, vous vous
remettez frénétiquement à chercher le pont invisible.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None:
        if roll <= 4:
            st.write_stream(stream_text('Si le chiffre que vous avez tiré est compris entre 0 et 4, rendez-vous au :'))
            st.page_link("tomes/tome7/page_344.py", label="344", icon="📄")
        else:
            st.write_stream(stream_text('Si ce chiffre est compris entre 5 et 9, rendez-vous au :'))
            st.page_link("tomes/tome7/page_58.py", label="58", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
