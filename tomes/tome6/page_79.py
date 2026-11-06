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

check_inventory(current_page_number=79, book=6)

fr_text = """
Vous passez devant de nombreux soldats de races et de
nationalités différentes qui se prélassent sur le pas des portes
ou bien sont adossés contre les murs en briques rouges des
maisons qui bordent la rue. Ce sont des mercenaires, attirés à
Varetta par les rumeurs de guerre qui se sont répandues jusqu'au
nord. Tous ces hommes ont accouru ici dans l'espoir de trouver
un emploi, prêts à vendre leurs talents de guerriers à n'importe
quelle cause. Sous une lanterne en fer noir, vous remarquez un
attroupement : quelques hommes jouent aux dés près d'un mur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez vous arrêter pour leur demander la direction de la rue des Chaudronniers, rendez-vous au :"))
    st.page_link("tomes/tome6/page_291.py", label="291", icon="📄")

    st.write_stream(stream_text("Si vous préférez passer votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome6/page_307.py", label="307", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
