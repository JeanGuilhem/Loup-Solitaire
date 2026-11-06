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

check_inventory(current_page_number=338, book=6)

fr_text = """
Vous sortez du château et embrassez du regard la vallée en
contrebas. Votre cœur bondit dans votre poitrine : votre
compagnon de voyage est aux prises avec six cavaliers revêtus
d'armures. Il est bientôt complètement encerclé, et ses efforts
pour résister sont désespérés. Frappé derrière la tête, il
s'effondre inconscient sur l'encolure de son cheval. Peu après, les
cavaliers s'enfuient sur la grand-route vers l'ouest avec leur
prisonnier. Lorsque vous atteignez le croisement avec la grand-
route, les cavaliers ne sont plus que de petits points à l'horizon.
Vous vous élancez vers votre monture avant qu'ils ne
disparaissent mais, alors que vous saisissez les rênes, vous
remarquez que le bâton en chêne de Cyrilus est tombé pendant
l'échauffourée. Vous le récupérez avant d'éperonner
vigoureusement les flancs de votre cheval.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_39.py", label="39", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
