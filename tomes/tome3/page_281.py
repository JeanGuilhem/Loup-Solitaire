import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=281, book=3)

fr_text = """
Vous vous enfouissez le nez dans votre manche et vous vous
détournez de la carcasse. Irian a repris connaissance et il se hâte
de plonger à son tour les mains dans l'huile de Bakanal dont il
s'enduit également le corps. Le jour tombe vite et vous décidez
d'établir votre campement ici même. Un repas est bientôt
préparé et, après avoir mangé, vous vous portez volontaire pour
monter la garde au cas où des Bakanals reviendraient. Vous
préférez de beaucoup, en effet, passer une nuit sans dormir en
bravant le souffle du vent plutôt que de dormir sous la tente,
dans l'effroyable odeur d'huile de Bakanal que dégagent vos guides.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_325.py", label="325", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
