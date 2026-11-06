import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

# Sans Pièce d'Or, le livre renvoie au 91 : les choix payants (172, 232) sont alors grisés.

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=332, book=6)

fr_text = """
Vous débouchez dans une large rue très sombre. Des lanternes
en fer forgé oscillent en grinçant au-dessus des portes des
boutiques et des habitations, noircissant les murs de leurs
fumées huileuses. La rue descend vers la Quarle, où sont
amarrées les péniches des riches marchands de la ville. Au nord
de Quarlen, la rivière n'est plus navigable et c'est ici que
s'effectue la jonction entre la Quarle et les routes de Casiorn et
des régions des Fins de Terre, qui assurent le ravitaillement de la
cité. A l'entrée d'un large pont de pierre se trouve une imposante
auberge comprenant des écuries et des bâtiments annexes. Un
bouclier peint accroché au-dessus du porche d'entrée de la cour
tient lieu d'enseigne, et vous pouvez lire, inscrit en grosses lettres :

**AUBERGE DU BOUT DU PONT**

A peine avez-vous franchi le porche qu'un garçon d'écurie
s'avance vers vous en vous adressant un petit signe de bienvenue.
Il vous montre la porte de l'auberge puis emmène votre cheval
par la bride. La salle est bondée en dépit de l'heure tardive. Un
feu de bois crépite dans l'immense cheminée de granit et une
alléchante odeur de bœuf rôti vous rappelle que vous n'avez rien
mangé de la journée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez vous attabler, rendez-vous au :'))
    if st.session_state.purse > 0:
        st.page_link("tomes/tome6/page_172.py", label="172", icon="📄")
    else:
        st.page_link("tomes/tome6/page_172.py", label="172", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous préférez vous diriger vers le patron pour vous enquérir d'une chambre pour la nuit, rendez-vous au :"))
    if st.session_state.purse > 0:
        st.page_link("tomes/tome6/page_232.py", label="232", icon="📄")
    else:
        st.page_link("tomes/tome6/page_232.py", label="232", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez aucune Pièce d'Or, rendez-vous au :"))
    if st.session_state.purse > 0:
        st.page_link("tomes/tome6/page_91.py", label="91", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_91.py", label="91", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Magnakaï de l'Intuition ou de l'Exploration, rendez-vous au :"))
    if has_magnakai("Intuition") or has_magnakai("Exploration"):
        st.page_link("tomes/tome6/page_346.py", label="346", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_346.py", label="346", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
