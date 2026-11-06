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

check_inventory(current_page_number=68, book=6)

fr_text = """
Alors que vous longez la rive, vous étudiez la carte des Pays de
la Storn afin de choisir le meilleur trajet pour atteindre
Tekaro. Deux routes peuvent vous y conduire : la grand-route
traversant les montagnes des Ceners, via Rhem, ou bien la
grand-route de la vallée, via Amory et la forêt d'Eula. Mais le
manque de sommeil et la fatigue occasionnée par votre longue
chevauchée vous obscurcissent l'esprit, aussi préférez-vous,
avant de prendre une décision, vous accorder une bonne nuit de
repos. Sur le quai, le panonceau prometteur d'une auberge vante
les lits les plus confortables de tout Soren. Voilà justement
tout ce dont vous avez besoin ! Après avoir conduit votre cheval
à l'écurie, vous poussez la porte de l'établissement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_167.py", label="167", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
