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

check_inventory(current_page_number=99, book=7)

fr_text = """
Vous sentez qu'il fait nettement plus chaud dans le tunnel nord
que dans le tunnel ouest. A en juger par l'odeur de soufre qui
s'infiltre jusque dans la caverne, il doit y avoir un phénomène
volcanique en action vers le nord.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez aller examiner ce qui se passe au nord, rendez-vous au :"))
    st.page_link("tomes/tome7/page_59.py", label="59", icon="📄")

    st.write_stream(stream_text("Si vous estimez plus prudent de prendre le tunnel ouest, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
