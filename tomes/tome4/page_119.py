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

check_inventory(current_page_number=119, book=4)

fr_text = """
« Plus un geste, Barraka ! Sa vie ne t'appartient pas ! » Vos
paroles ont résonné en dominant le mugissement du vent. Le
renégat se tourne pour vous faire face en éclatant d'un rire aussi
sonore que votre ordre. Il s'avance alors vers vous en serrant
dans son poing le poignard à la lame enflammée. Vous dégainez
votre arme et vous entrez dans le temple.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez engager le combat avec ce Seigneur de la Guerre, rendez-vous au :'))
    st.page_link("tomes/tome4/page_296.py", label="296", icon="📄")

    st.write_stream(stream_text('Si vous préférez essayer de libérer Madelon, rendez-vous au :'))
    st.page_link("tomes/tome4/page_73.py", label="73", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
