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

check_inventory(current_page_number=236, book=5)

fr_text = """
Emporté par votre élan, vous traversez rapidement la passerelle
sans être repéré. Lorsque vous portez votre coup, le Garde est
toujours à genoux, en train de ramasser son or éparpillé sur le
sol. Votre attaque est silencieuse et mortelle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez fouiller le corps du Garde, rendez-vous au :"))
    st.page_link("tomes/tome5/page_207.py", label="207", icon="📄")

    st.write_stream(stream_text("Si la dépouille ne vous intéresse pas, hâtez-vous de gagner l'enclos de l'Itikar et rendez-vous au :"))
    st.page_link("tomes/tome5/page_224.py", label="224", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
