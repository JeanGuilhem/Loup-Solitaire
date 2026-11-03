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

check_inventory(current_page_number=131, book=4)

fr_text = """
La porte n'est pas fermée à clé. Vous l'ouvrez et vous pénétrez
dans un tunnel plongé dans la pénombre. Cette partie de la mine
semble avoir été creusée récemment. Les étais sont neufs en
effet, et le sol n'a pas encore été égalisé par le passage répété des
mineurs et des chariots. Ce tunnel mène vers le sud sur 1
kilomètre et demi. Puis soudain, il tourne brusquement vers
l'ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_185.py", label="185", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
