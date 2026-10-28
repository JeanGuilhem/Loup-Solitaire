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

check_inventory(current_page_number=131, book=3)

fr_text = """
Vous sentez que ces boutons commandent quelque ancien
mécanisme et que, si on appuie dessus dans le bon ordre, une
quelconque cachette, coffre ou compartiment secret, sera
dévoilée. Mais il se peut aussi qu'en appuyant dessus dans le
mauvais ordre ils déclenchent un piège.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez appuyer sur ces boutons, rendez-vous au :"))
    st.page_link("tomes/tome3/page_227.py", label="227", icon="📄")
    st.write_stream(stream_text("Si vous ne voulez pas prendre le risque d'actionner un piège, vous pouvez quitter le temple en vous rendant au :"))
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
