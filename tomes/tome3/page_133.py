import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=133, book=3)

fr_text = """
Une coupe de M'iare est suspendue au plafond, juste au-dessus
de la crevasse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer d'attacher votre Corde à cette coupe pour vous élancer ensuite de l'autre côté, rendez-vous au :"))
    if has_item("CORDE"):
        st.page_link("tomes/tome3/page_201.py", label="201", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_201.py", label="201", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne voulez pas prendre le risque de tomber dans la crevasse, vous devrez revenir sur vos pas et emprunter un autre chemin en vous rendant au :"))
    st.page_link("tomes/tome3/page_297.py", label="297", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
