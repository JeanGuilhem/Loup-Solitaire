import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=347, book=6)

fr_text = """
En pariant, vous avez attiré l'attention de deux mercenaires au
regard inquisiteur qui vous surveillent depuis votre arrivée à
l'Auberge des Épées Croisées. A la fin de ce spectacle peu
recommandable, la foule se disperse peu à peu et vous sentez la
pointe d'un couteau contre votre colonne vertébrale. « La bourse
ou la vie ! murmure l'un des hommes en vous soufflant son
haleine fétide au visage. Décide-toi vite ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous vous résignez à lui donner toutes vos Pièces d'Or sans offrir la moindre résistance, rendez-vous au :"))
    if st.session_state.purse > 0:
        st.page_link("tomes/tome6/page_161.py", label="161", icon="📄")
    else:
        st.page_link("tomes/tome6/page_161.py", label="161", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous refusez d'obtempérer, préparez-vous à défendre chèrement votre bien et rendez-vous au :"))
    st.page_link("tomes/tome6/page_282.py", label="282", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, rendez-vous au :"))
    if has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_114.py", label="114", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_114.py", label="114", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
