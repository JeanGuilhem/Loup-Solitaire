import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=344, book=3)

fr_unknown_item = "Vous ne possédez pas cet objet."
fr_has_triangle = "Vous possédez un Triangle de Pierre Bleue."

fr_text = """
La porte de la forteresse est complètement lisse et ne comporte
apparemment ni serrure, ni gond, ni trou de serrure. En
examinant le mur d'à côté, vous découvrez cependant que l'un
des blocs qui le constituent est différent des autres : un petit
triangle est en effet gravé à sa surface.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Triangle de Pierre Bleue, rendez-vous au :"))
    if has_item("TRIANGLE DE PIERRE BLEUE"):
        st.page_link("tomes/tome3/page_41.py", label="41", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_41.py", label="41", icon="📄", disabled=True)
    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    if not has_item("TRIANGLE DE PIERRE BLEUE"):
        st.page_link("tomes/tome3/page_147.py", label="147", icon="📄")
    else:
        st.write_stream(stream_text(fr_has_triangle))
        st.page_link("tomes/tome3/page_147.py", label="147", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
