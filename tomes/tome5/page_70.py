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

check_inventory(current_page_number=70, book=5)

fr_text = """
Vous poursuivez rapidement votre chemin et vous avez parcouru
environ un 1,5 km lorsque vous atteignez une énorme herse en
fer qui bloque complètement le tunnel. La carcasse décomposée
d'un Lézard Géant est écrasée contre la grille. Le cadavre a été
dévoré et il ne reste plus sur les os mis à vif que quelques
lambeaux de chair pourrie. Les barreaux de la herse sont solides
et bien scellés, et il vous est par conséquent impossible de
continuer dans cette direction. Près de la dépouille du Lézard,
vous constatez qu'une étroite plateforme en pierre dépasse
légèrement du mur et mène à un petit passage voûté et sombre
au bout duquel se trouve un escalier montant vers la surface.
Soudain, la voix forte de Maouk retentit dans le tunnel. Il exhorte
ses Sharnazims à presser le pas dans votre direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez monter l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_43.py", label="43", icon="📄")

    st.write_stream(stream_text("Si vous préférez attendre sur place pour affronter vos poursuivants, rendez-vous au :"))
    st.page_link("tomes/tome5/page_60.py", label="60", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
