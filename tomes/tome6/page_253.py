import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=253, book=6)

fr_text = """
« Eh bien, vous êtes arrivé juste à temps ! dit le jovial
aubergiste en regardant par la fenêtre les gros nuages noirs qui
s'amoncellent. La nuit promet d'être agitée. Y'a pas de doute ! »
Vous prenez une chambre contre 2 Pièces d'Or pour la nuit, plus 1
Pièce d'Or pour votre cheval. Un Repas composé d'œufs durs et de
pain noir vous coûtera 1 Pièce d'Or, mais vous pouvez prendre
aussi 1 Repas de votre Sac à Dos. Si vous ne mangez pas
maintenant, vous perdez 3 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas(gold_cost=1)

    st.write_stream(stream_text("Si vous souhaitez payer l'aubergiste pour la nuit (3 Pièces d'Or), rendez-vous au :"))
    if st.button("Payer 3 Pièces d'Or", disabled=st.session_state.purse < 3):
        spend_gold(3)
        st.switch_page("tomes/tome6/page_35.py")

    st.write_stream(stream_text("Si vous n'avez pas assez de Pièces d'Or pour vous payer une chambre, rendez-vous au :"))
    if st.session_state.purse < 3:
        st.page_link("tomes/tome6/page_54.py", label="54", icon="📄")
    else:
        st.page_link("tomes/tome6/page_54.py", label="54", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
