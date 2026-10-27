import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=39, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
A la tombée du jour, la diligence s'arrête devant une auberge sur la
route qui longe la côte en direction de Port Bax. Le prix d'une chambre
pour la nuit s'élève à 1 Couronne d'Or pour les passagers de la diligence
et à 3 Couronnes pour les autres clients. Au moment où vous vous
apprêtez à entrer, le conducteur de la diligence vous demande votre
billet.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez un billet pour Port Bax, rendez-vous au :"))
    if has_item("BILLET DE DILIGENCE"):
        st.page_link("tomes/tome2/page_346.py", label="346", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_346.py", label="346", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous n'avez pas de billet, rendez-vous au :"))
    st.page_link("tomes/tome2/page_156.py", label="156", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
