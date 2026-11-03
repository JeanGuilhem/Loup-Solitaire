import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=322, book=4)

fr_text = """
Vous éteignez votre Torche et vous vous pelotonnez sur le sol,
sombrant très vite dans un profond sommeil. Lorsque vous vous
réveillez, plusieurs heures plus tard, vous vous sentez tout à fait
reposé et vous regagnez 2 points d'ENDURANCE. Vous rallumez
votre Torche et vous constatez alors que la petite cabane bâtie
contre le mur est remplie d'outils. Des Pioches, des Pelles et des
brouettes sont entassées au fond. Si vous souhaitez prendre une
Pioche ou une Pelle, notez-la sur votre Feuille d'Aventure dans la
case objets contenus dans votre Sac à Dos. Étant donné la taille
de ces outils, ils occupent chacun la place de deux objets
normaux. Deux tunnels permettent de sortir de la salle, l'un
orienté à l'ouest, l'autre au sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=2)

    pickup_button("PIOCHE", key="outil", label="Prendre une Pioche")
    pickup_button("PELLE", key="outil", label="Prendre une Pelle")

    st.write_stream(stream_text("Si vous souhaitez emprunter le tunnel qui mène vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome4/page_54.py", label="54", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre celui orienté au sud, rendez-vous au :"))
    st.page_link("tomes/tome4/page_129.py", label="129", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
