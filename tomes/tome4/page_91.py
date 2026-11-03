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

check_inventory(current_page_number=91, book=4)

fr_text = """
Il est impossible de pénétrer à cheval dans la mine et vous êtes
donc contraints d'abandonner vos montures à l'extérieur. Les
galeries sont totalement obscures mais vous remarquez bientôt
que des Torches éteintes sont fixées aux murs à intervalles
réguliers. Vos hommes et vous-même prenez chacun une Torche
que vous allumez avant de poursuivre votre chemin. Dans la
faible clarté qu'elles diffusent vous découvrez des traces de pas
menant vers un endroit où le tunnel s'est éboulé. Les traces se
poursuivent jusqu'au sommet d'un énorme tas de terre qui
atteint presque le plafond, ne laissant qu'une petite ouverture
entre les deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez escalader ce tas de terre et vous glisser dans l'ouverture, rendez-vous au :"))
    st.page_link("tomes/tome4/page_254.py", label="254", icon="📄")

    st.write_stream(stream_text("Si vous préférez renoncer à cette exploration, vous pouvez ressortir, reprendre vos chevaux et descendre le sentier de la colline en vous rendant au :"))
    st.page_link("tomes/tome4/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
