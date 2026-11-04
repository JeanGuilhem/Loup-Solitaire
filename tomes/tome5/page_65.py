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

check_inventory(current_page_number=65, book=5)

fr_text = """
L'un des Gardes s'écroule, frappé à mort par le coup que vous lui
avez asséné sur la nuque du tranchant de la main, mais en vous
retournant, vous voyez soudain que l'autre Garde a repris
connaissance et rampe péniblement sur le sol pour tenter de
récupérer son épée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez achever ce Garde immédiatement, rendez-vous au :"))
    st.page_link("tomes/tome5/page_78.py", label="78", icon="📄")

    st.write_stream(stream_text("Si vous préférez le maîtriser et le capturer vivant, rendez-vous au :"))
    st.page_link("tomes/tome5/page_199.py", label="199", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
