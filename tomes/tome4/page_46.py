import streamlit as st
from combat import combat
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

check_inventory(current_page_number=46, book=4)

fr_text = """
Vous avez à peine fait une dizaine de pas qu'une vision effrayante
s'offre soudain à vos yeux. Le tunnel, en effet, est bloqué un peu
plus loin par une créature énorme et gluante dont la peau est
couverte de verrues qui brillent d'une lueur verdâtre. Vous
dégainez votre arme tandis que le monstre avance par bonds sur
ses pattes crochues. Soudain, deux ailes surgissent sur son dos,
et il s'élance dans l'air. Sa gueule ouverte découvre une rangée de
dents tranchantes comme des rasoirs. La créature fond sur vous
et il vous faut la combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DÉMONDES SOUTERRAINS", 20, 10)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome4/page_281.py", label="281", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
