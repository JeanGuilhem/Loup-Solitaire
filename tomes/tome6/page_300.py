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

check_inventory(current_page_number=300, book=6)

fr_text = """
Vous avancez au pas, le long d'une large avenue au pavé rouge
délavé par les intempéries. Vous admirez la ville qui s'éveille
dans la lumière du petit matin. Les habitants commencent à ouvrir
leurs volets et les odeurs délicieuses de petit déjeuner et du
pain encore chaud emplissent l'air. Vous arrivez bientôt au centre
de la ville. Vous traversez une place pavée de dalles en cristal
et vous passez sous une arche construite en pierre verte polie par
les ans. Les imposants palais et les grands bâtiments publics font
place maintenant à des échoppes poussiéreuses. Vous longez un parc
rempli de fleurs magnifiques aux immenses feuilles rouges, or et
roses, puis vous suivez une rue de gravier blanc qui mène à une
tour fortifiée : le plus haut édifice de la ville. C'est la Tour
du Roi, au-delà de laquelle se trouve la rue des Chaudronniers.
Vous êtes enfin arrivé ! Vous entendez le doux murmure argentin
des fontaines et apercevez des vieillards vêtus d'une robe marron,
la tête recouverte d'un capuchon, qui avancent silencieusement
dans l'allée de gravier blanc. Vous entrez sous un porche et vous
vous retrouvez dans la cour d'un grand bâtiment. Tout à coup, un
frisson d'excitation vous parcourt le dos: vous touchez presque au
but. Au centre de la cour se trouve un plan détaillé des lieux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous diriger vers l'observatoire, rendez-vous au :"))
    st.page_link("tomes/tome6/page_127.py", label="127", icon="📄")

    st.write_stream(stream_text("Si vous choisissez d'aller à la bibliothèque, rendez-vous au :"))
    st.page_link("tomes/tome6/page_21.py", label="21", icon="📄")

    st.write_stream(stream_text("Enfin, si vous préférez visiter le temple, rendez-vous au :"))
    st.page_link("tomes/tome6/page_320.py", label="320", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
