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

check_inventory(current_page_number=144, book=7)

fr_text = """
Vous continuez à avancer dans le tunnel jusqu'à ce que vous
arriviez à un cul-de-sac. La lueur rouge que vous aperceviez tout
à l'heure se déverse à flots par un portail étroit comme une fente.
En regardant à travers, vous assistez à un spectacle
impressionnant: un énorme cratère de fer noir descend par
paliers successifs jusqu'à un sol couleur de sang. Des centaines
de silhouettes s'activent sur chaque palier, poussant des chariots
et manœuvrant de monstrueuses machines sur des pans inclinés
et des passerelles reliant les différents degrés. Vous apercevez
également, au milieu de cette foule grouillante, de hautes
silhouettes en uniforme noir, qui font claquer leur fouet en
proférant des invectives. La chaleur torride et la vapeur qui
arrivent par vagues à travers le portail vous empêchent d'en voir
plus. Soudain, un lourd panneau de fer s'abat du plafond et vient
obstruer le portail. Vous reculez d'un bond et vous faites demi-
tour mais, à travers la fumée qui envahit le passage, vous voyez
s'abattre au loin un second panneau de fer, bloquant l'issue de
l'autre côté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_37.py", label="37", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
