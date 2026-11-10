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

check_inventory(current_page_number=188, book=7)

fr_text = """
Vous plongez dans l'espace qui se réduit maintenant à quelques
dizaines de centimètres et vous entendez, juste après, le mur
s'abattre derrière vous dans un énorme craquement. Vous êtes
étendu sur le dos, le cœur battant à tout rompre et l'estomac
noué à la pensée d'avoir frôlé la mort de si près. Vous vous
remettez péniblement sur vos pieds et vous continuez à avancer
le long du tunnel qui est, maintenant, sensiblement plus froid et
plus dégagé qu'auparavant. Vous arrivez bientôt dans une salle
d'où se dégage une forte odeur d'humus. Le plafond est soutenu
par deux rangées de piliers en pierre et, au milieu de la pièce, se
dresse un immense sarcophage en granit. Tout à coup, vous
entendez un cliquetis d'armure et des bruits de pas qui se
rapprochent de l'entrée d'un tunnel à votre droite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous cacher derrière l'un des piliers, rendez-vous au :"))
    st.page_link("tomes/tome7/page_110.py", label="110", icon="📄")

    st.write_stream(stream_text("Si vous voulez quitter la salle par un tunnel s'ouvrant sur votre gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_201.py", label="201", icon="📄")

    st.write_stream(stream_text("Si vous préférez tendre une embuscade à qui s'approche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_319.py", label="319", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
