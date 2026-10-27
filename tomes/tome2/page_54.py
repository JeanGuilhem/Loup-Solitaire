import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=54, book=2)

fr_text = """
Au moment où vous franchissez la porte en courant, une lance
s'enfonce dans votre poitrine avec une telle force que vous en êtes
soulevé de terre. Le clair de lune s'estompe et la dernière vision que
vous emporterez de ce monde n'a rien de réconfortant: les visages
grimaçants de villageois réunis en cercle se penchent sur vous et des
dizaines de mains vous poignardent à mort. Votre quête s'achève ici en
même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
