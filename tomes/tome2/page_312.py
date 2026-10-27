import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=312, book=2)

fr_text = """
Lorsque l'aube se lève, il fait froid et la pluie tombe à verse ; votre cape
de Seigneur Kaï et l'abri du feuillage vous ont cependant protégé en
vous tenant au chaud et au sec la nuit durant. Vous jetez un coup d'œil à
la route qui longe la côte et vous apercevez au loin une diligence qui
avance dans votre direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez descendre de l'arbre et faire signe au conducteur de l'attelage, rendez-vous au :"))
    st.page_link("tomes/tome2/page_117.py", label="117", icon="📄")
    st.write_stream(stream_text("Si vous préférez essayer de sauter sur le toit de la diligence lorsqu'elle passera sous les branches de l'arbre, rendez-vous au :"))
    st.page_link("tomes/tome2/page_89.py", label="89", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
