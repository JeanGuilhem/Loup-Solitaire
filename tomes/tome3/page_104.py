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

check_inventory(current_page_number=104, book=3)

fr_text = """
Vous arrivez enfin devant une grande porte de pierre. A la
différence des autres, celle-ci n'est pas actionnée par un levier
mais vous remarquez en revanche une petite fente creusée dans
le mur, juste à côté de la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_item("DISQUE DE PIERRE BLEUE"):
        st.write_stream(stream_text("Si vous possédez un Disque de Pierre Bleue, rendez-vous au :"))
        st.page_link("tomes/tome3/page_135.py", label="135", icon="📄")
    else:
        st.write_stream(stream_text("Si vous possédez un Disque de Pierre Bleue, rendez-vous au :"))
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_135.py", label="135", icon="📄", disabled=True)
        st.write_stream(stream_text("Dans le cas contraire, il vous faudra rebrousser chemin le long du couloir et prendre la direction du sud en vous rendant au :"))
        st.page_link("tomes/tome3/page_330.py", label="330", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
