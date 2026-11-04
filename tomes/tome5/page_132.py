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

check_inventory(current_page_number=132, book=5)

fr_text = """
Vous avancez rapidement et sans difficulté dans la galerie nord et
vous arrivez bientôt à un autre passage voûté qui va vers l'ouest.
Vous apercevez une lueur qui brille au loin et vous entendez le
bruit caractéristique du métal chauffé à blanc que l'on plonge
dans l'eau et les coups violents d'un marteau sur une enclume. Il
s'agit sans aucun doute d'une forge.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez approcher de la forge, rendez-vous au :"))
    st.page_link("tomes/tome5/page_195.py", label="195", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer vers le nord, rendez-vous au :"))
    st.page_link("tomes/tome5/page_30.py", label="30", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
