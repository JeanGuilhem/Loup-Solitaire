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

check_inventory(current_page_number=235, book=6)

fr_text = """
Dans la semi-obscurité de l'égout, vous distinguez à peine les
rues de Tekaro sur votre carte. La cathédrale est en plein centre
de la ville, à moins d'un kilomètre du point de jonction des deux
rivières et se trouve plein est par rapport à l'endroit où vous avez
pénétré dans les égouts. Vous repliez la carte et vous vous dirigez
vers votre but.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_269.py", label="269", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
