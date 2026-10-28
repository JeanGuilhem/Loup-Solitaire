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

check_inventory(current_page_number=315, book=3)

fr_text = """
Vous arrivez bientôt dans une vaste caverne où, sous la pression
de la glace en mouvement, une immense crevasse s'est ouverte
dans le sol. Elle fait une vingtaine de mètres de large et il n'y a
apparemment aucun moyen de la traverser. En jetant un coup
d'œil dans le gouffre, vous remarquez que des marches ont été
grossièrement taillées dans la paroi, permettant ainsi de
descendre dans les ténèbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez descendre ces marches, rendez-vous au :"))
    st.page_link("tomes/tome3/page_302.py", label="302", icon="📄")
    st.write_stream(stream_text("Si vous préférez revenir sur vos pas en direction de l'autre tunnel, rendez-vous au :"))
    st.page_link("tomes/tome3/page_125.py", label="125", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
