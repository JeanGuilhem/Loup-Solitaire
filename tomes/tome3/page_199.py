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

check_inventory(current_page_number=199, book=3)

fr_text = """
Au bout d'un kilomètre et demi environ, le tunnel aux murs de
glace aboutit à une grotte magnifique. De la neige fondue coule
en cascade sur des rocs argentés, projetant alentour des reflets
éblouissants. Sous la cascade s'ouvre une petite grotte qui
disparaît dans la paroi rocheuse aux éclats d'argent. Il ne semble
pas qu'il y ait d'autre chemin pour quitter cette caverne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez pénétrer dans la petite grotte, rendez-vous au :'))
    st.page_link("tomes/tome3/page_82.py", label="82", icon="📄")
    st.write_stream(stream_text("Si vous préférez revenir sur vos pas et prendre l'autre tunnel, rendez-vous au :"))
    st.page_link("tomes/tome3/page_284.py", label="284", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
