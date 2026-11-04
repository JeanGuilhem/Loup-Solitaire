import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=72, book=5)

fr_text = """
« Allez-vous-en ! crie la tenancière grassouillette de la taverne.
Ici, nous n'aimons pas les gens qui manquent de respect à notre
défunt Zakhan. » Deux hommes solidement charpentés, portant
chacun un brassard de crêpe noir, vous poussent brutalement
vers la porte et vous tombez en glissant sur les pavés sales de la
rue. Vous vous éraflez la hanche et les coudes dans votre chute et
vous perdez 1 point d'ENDURANCE. Au moment où vous vous
relevez, Maouk et ses hommes surgissent soudain sur la place et
vous encerclent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
    st.write_stream(stream_text("Si vous voulez les affronter, rendez-vous au :"))
    st.page_link("tomes/tome5/page_36.py", label="36", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous rendre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
