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

check_inventory(current_page_number=30, book=3)

fr_text = """
Le passage se prolonge tout droit pendant quelques mètres, puis
il tourne brusquement vers l'est. Un peu plus loin, vous
apercevez une lueur qui filtre à travers une fente dans le mur. En
y regardant de plus près, vous découvrez une porte secrète et un
petit levier de pierre. Vous tirez sur le levier et la porte s'ouvre
aussitôt en glissant latéralement, révélant un large couloir bien
éclairé. A votre gauche, à moins de 10 mètres, vous remarquez un
croisement. A votre droite, vous voyez une porte de pierre
fermée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez examiner cette porte, rendez-vous au :'))
    st.page_link("tomes/tome3/page_203.py", label="203", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous diriger vers le croisement, rendez-vous au :'))
    st.page_link("tomes/tome3/page_276.py", label="276", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
