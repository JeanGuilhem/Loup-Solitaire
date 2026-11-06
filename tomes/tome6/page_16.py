import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=16, book=6)

fr_text = """
A la faible lueur d'une lanterne accrochée dans la rue, vous
dépliez le plan de Varetta et vous étudiez le dédale de ruelles et
d'avenues qui quadrillent la ville. (Inscrivez cette carte dans la
case Objets Spéciaux de votre Feuille d'Aventure.) La rue des
Chaudronniers est située à l'autre bout de la ville, non loin du
rempart est. Soudain, une cloche se met à sonner et l'écho de son
tintement se répercute de toit en toit, de tour en tour, à travers
toute la cité. C'est le couvre-feu : il ne devra plus rester
personne dans les rues d'ici à une heure. Comme il vous est
impossible de traverser Varetta en si peu de temps, vous décidez
de trouver une auberge afin d'y passer la nuit et de reprendre
votre route dès l'aube.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page() and not has_item("PLAN DE VARETTA"):
        add_to_inventory("PLAN DE VARETTA")
    st.success("Le Plan de Varetta est inscrit dans vos Objets Spéciaux.")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_135.py", label="135", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
