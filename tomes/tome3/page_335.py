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

check_inventory(current_page_number=335, book=3)

fr_text = """
La paroi glacée offre de nombreuses prises, mais vous ne pouvez
pas vous y agripper tant que vous portez vos moufles ; en
revanche, si vous ôtez vos moufles, vous aurez sans nul doute à
subir la morsure du gel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez risquer votre vie et vos mains, vous pouvez entreprendre l'escalade en vous rendant au :"))
    st.page_link("tomes/tome3/page_55.py", label="55", icon="📄")
    st.write_stream(stream_text("Si vous préférez y renoncer, vous pouvez essayer de trouver une issue pour quitter la caverne en vous rendant au :"))
    st.page_link("tomes/tome3/page_182.py", label="182", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
