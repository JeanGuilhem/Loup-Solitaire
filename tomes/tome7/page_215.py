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

check_inventory(current_page_number=215, book=7)

fr_text = """
Vous commencez à examiner l'horrible main, mais elle vous
saute brusquement au visage. Vous poussez un cri de terreur et
vous parez instinctivement son attaque en la frappant
violemment. La main est projetée en arrière et se dirige en
tournoyant vers les piliers verts. Mais, juste au moment où elle
arrive à leur niveau, elle explose et est complètement pulvérisée.
Vous avez enfin triomphé de la main qui s'est désintégrée au
contact de l'invisible barrière d'énergie destructrice située entre
les colonnes. Satisfait et soulagé, vous vous dirigez vers le
passage au fond de la pièce.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_334.py", label="334", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
