import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=269, book=2)

fr_text = """
La vision répugnante de la créature qui se tortille sur le sol vous remplit
de dégoût pour les Maîtres des Ténèbres et leurs immondes séides.
Lorsque enfin le Monstre d'Enfer s'est entièrement décomposé et que
vous êtes sûr de l'avoir anéanti à tout jamais, vous arrachez de ses
restes la Lance Magique dont vous essuyez le fer sur l'étoffe fumante
de ses vêtements. Vous avez hâte de quitter cet endroit et vous courez
le long du tunnel aussi vite que possible.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_349.py", label="349", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
