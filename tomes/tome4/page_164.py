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

check_inventory(current_page_number=164, book=4)

fr_text = """
Soudain, le son aigu d'une corne de guerre vous glace le sang. Des
Guerriers Pillards vêtus d'habits écarlates sautent alors des
feuillages et se précipitent sur vos hommes. Ils sont trois fois
plus nombreux que vous et il se pourrait bien qu'il soit
impossible d'échapper à cette mortelle embuscade.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez rassembler vos hommes pour engager le combat, rendez-vous au :'))
    st.page_link("tomes/tome4/page_299.py", label="299", icon="📄")

    st.write_stream(stream_text('Si vous préférez leur ordonner de battre immédiatement en retraite et de se réfugier dans la mine, rendez-vous au :'))
    st.page_link("tomes/tome4/page_52.py", label="52", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
