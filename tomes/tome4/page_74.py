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

check_inventory(current_page_number=74, book=4)

fr_text = """
La nuit se déroule sans incident et vous vous sentez bien reposé
après ces heures de sommeil. Vous gagnez aussitôt 1 point
d'ENDURANCE. Vous levez le camp, puis vous pénétrez dans la
forêt qui s'étend sur les versants de la vallée. Votre instinct de
guerrier vous avertit que la grand-route constitue un lieu idéal
pour une embuscade. Les arbres au feuillage dense qui la
bordent offrent en effet une excellente cachette pour d'éventuels
agresseurs. Afin de prévenir une attaque surprise, vous envoyez
trois de vos hommes en reconnaissance avec ordre de signaler
tout élément suspect. Après avoir parcouru une certaine
distance, vous découvrez la carcasse d'un chariot calciné
abandonné sur le bas-côté de la route. Derrière, un sentier
s'éloigne vers l'est en remontant les collines. Vos éclaireurs, qui
auraient dû vous informer de l'existence du chariot, n'ont pas
donné signe de vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=1)

    st.write_stream(stream_text("Si vous souhaitez examiner les débris du chariot, rendez-vous au :"))
    st.page_link("tomes/tome4/page_38.py", label="38", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas y prêter attention et poursuivre votre chemin le long de la route, rendez-vous au :"))
    st.page_link("tomes/tome4/page_175.py", label="175", icon="📄")

    st.write_stream(stream_text("Enfin, si vous souhaitez explorer le sentier qui mène dans les collines, rendez-vous au :"))
    st.page_link("tomes/tome4/page_293.py", label="293", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
