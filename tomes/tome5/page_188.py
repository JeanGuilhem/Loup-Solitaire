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

check_inventory(current_page_number=188, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
La taverne est bondée. Les consommateurs sont accoudés à un
long comptoir de pierre incrusté de fragments de marbre aux
couleurs variées. De grandes jarres en terre cuite remplies de
divers plats épicés sont posées sur le comptoir et des serveuses
vont et viennent, tâchant de satisfaire les clients impatients.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous portez un Brassard noir, rendez-vous au :'))
    if has_item("BRASSARD NOIR"):
        st.page_link("tomes/tome5/page_172.py", label="172", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_172.py", label="172", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'en possédez pas, rendez-vous au :"))
    if not has_item("BRASSARD NOIR"):
        st.page_link("tomes/tome5/page_72.py", label="72", icon="📄")
    else:
        st.page_link("tomes/tome5/page_72.py", label="72", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
