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

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=229, book=3)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous reconnaissez ce serpent : c'est un Javek, un serpent des
glaces à deux têtes, et au venin mortel. Tandis qu'il ondule vers
vous, vous voyez s'ouvrir la gueule de sa seconde tête et vous
distinguez nettement ses crochets jaunes à l'extrémité desquels
perle une goutte de venin. La créature se déplace très rapidement
et vous avez parfaitement conscience que vous ne pourrez pas la
distancer sur cette corniche étroite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Sphère de Feu, rendez-vous au :"))
    if has_item("SPHÈRE DE FEU"):
        st.page_link("tomes/tome3/page_46.py", label="46", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_46.py", label="46", icon="📄", disabled=True)
    st.write_stream(stream_text("Sinon, il faut vous préparer au combat et vous rendre au :"))
    st.page_link("tomes/tome3/page_88.py", label="88", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
