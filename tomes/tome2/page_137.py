import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=137, book=2)

fr_text = """
Vous arrivez à un croisement ; la rue du Mendiant tourne en direction
du sud et aboutit à la rue du Chevalier Noir. Quelques mètres plus loin,
une autre voie, la rue de l'Ancre, mène en direction de l'est. La pluie
tombe de plus en plus dru, à présent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez aller vers le sud le long de la rue du Chevalier Noir, rendez-vous au :"))
    st.page_link("tomes/tome2/page_259.py", label="259", icon="📄")
    st.write_stream(stream_text("Si vous préférez suivre la rue de l'Ancre en direction de l'est, rendez-vous au :"))
    st.page_link("tomes/tome2/page_20.py", label="20", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
