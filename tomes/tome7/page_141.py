import streamlit as st
from inventory import (
    check_inventory,
    completed_lore_circles,
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

check_inventory(current_page_number=141, book=7)

fr_text = """
Après avoir essuyé la sueur qui baigne votre visage d'un revers de
la manche, vous tournez les talons pour reprendre votre chemin
mais, ce faisant, vous butez sur un objet. Au premier regard, on
dirait une masse d'armes, mais en le regardant de plus près, vous
constatez qu'il s'agit d'un bâton en argent au bout duquel est
enchâssée une boule de verre orangé. L'objet paraît bien trop
délicat pour servir d'arme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez prendre le Sceptre d'Argent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_223.py", label="223", icon="📄")

    st.write_stream(stream_text("Si vous préférez le laisser là où il se trouve et continuer votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome7/page_308.py", label="308", icon="📄")

    st.write_stream(stream_text("Si vous avez complété le Cercle de l'Esprit, rendez-vous au :"))
    st.page_link("tomes/tome7/page_25.py", label="25", icon="📄", disabled=not ("Cercle de l'Esprit" in completed_lore_circles()))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
