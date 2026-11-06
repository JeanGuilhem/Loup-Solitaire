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

check_inventory(current_page_number=173, book=6)

fr_text = """
Vous remarquez que les vêtements et les cheveux de l'homme
sont maculés de sang. Vous vous apprêtez immédiatement à lui
porter secours mais, alors qu'il atteint le porche de l'église, vous
réalisez qu'il n'est pas blessé le moins du monde : les taches
rouges ne sont en réalité que du jus de myrtille, et ses blessures
sont contrefaites.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez défier l'homme en combat, rendez-vous au :"))
    st.page_link("tomes/tome6/page_337.py", label="337", icon="📄")

    st.write_stream(stream_text("Si vous préférez partir au galop pour vous éloigner de cette église le plus vite possible, rendez-vous au :"))
    st.page_link("tomes/tome6/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
