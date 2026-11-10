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

check_inventory(current_page_number=277, book=7)

fr_text = """
Vous avez à peine fait quelques pas que vous entendez un petit
bruissement. Vous regardez, horrifié, le sol se dérober sous vos
pieds et disparaître dans un trou noir et béant. Vous tombez dans
le vide, et votre tête heurte la saillie d'un rocher. Inconscient,
vous continuez à tomber comme une pierre dans les profondeurs
inconnues.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_164.py", label="164", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
