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

check_inventory(current_page_number=177, book=6)

fr_text = """
« Ah ! Vous avez de la chance, cette nuit, étranger. Les dés vous
sont favorables. » L'homme quelque peu éméché se lève avec
difficulté, puis vous indique en titubant une allée à quelques
mètres. « Vous voyez cette porte ? C'est là que demeurent les
crieurs publics. Ils vous diront où se trouve la rue des
Chaudronniers. » Vous inclinez la tête en signe de remerciement,
puis vous éperonnez votre cheval et vous vous dirigez dans
l'obscurité vers la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_25.py", label="25", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
