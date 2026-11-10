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

check_inventory(current_page_number=259, book=7)

fr_text = """
Grimaçant de dégoût, vous essuyez votre visage ruisselant du
sang du loup, puis vous faites demi-tour pour faire face aux
nombreuses bulles qui flottent dans le couloir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer de traverser cet amas de bulles, rendez-vous au :"))
    st.page_link("tomes/tome7/page_107.py", label="107", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez vous frayer un chemin à travers les bulles, mais à l'aide de votre épée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_151.py", label="151", icon="📄")

    st.write_stream(stream_text("Si vous préférez rebrousser chemin vers la pièce voûtée et emprunter l'autre tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
