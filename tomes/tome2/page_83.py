import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=83, book=2)

fr_text = """
Au bout de la rue de la Bernicle, vous arrivez à un croisement. Il fait
déjà nuit à présent et il va bientôt falloir vous trouver un abri.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez tourner à gauche, dans la rue du Tonnelier, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_227.py", label="227", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre à droite la rue de la Licorne, rendez-vous au :"))
    st.page_link("tomes/tome2/page_297.py", label="297", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
