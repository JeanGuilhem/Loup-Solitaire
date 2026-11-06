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

check_inventory(current_page_number=290, book=6)

fr_text = """
Vous entrez dans Eula aux côtés du Capitaine qui arbore une
bannière sur laquelle est brodé son emblème : une rutilante hache
de guerre. La ville s'est transformée en un immense camp
militaire. Tous ses habitants ont fui depuis longtemps vers le
nord, abandonnant maisons, vivres et biens aux soldats pilleurs.
Des hommes de toutes nationalités se sont mêlés aux guerriers dans
l'espoir d'obtenir une part du butin. Vous vous frayez un chemin
parmi les nombreux fantassins qui encombrent les rues et vous
apercevez, à quelques kilomètres au sud, la ville de Tekaro qui
brûle sous un épais nuage noir. Vous sentez alors votre cœur
défaillir : la Pierre de la Sagesse se trouve là-bas, dans une
ville assiégée par six mille combattants ! Vous approchez des
rives de la Quarle où l'on a commencé les travaux en vue du siège.
Le Capitaine vous montre sur la gauche un campement dressé dans un
champ. En haut d'un mât flotte un étendard bleu noirci par la suie
et orné d'un aigle doré. « L'Etendard du Prince Ewewin ! s'écrie
le Capitaine. Il est temps de rejoindre notre employeur ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez rester avec le Capitaine, rendez-vous au :"))
    st.page_link("tomes/tome6/page_204.py", label="204", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre congé des mercenaires, rendez-vous au :"))
    st.page_link("tomes/tome6/page_280.py", label="280", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
