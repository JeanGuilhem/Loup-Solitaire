import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=10, book=4)

fr_text = """
Le Guerrier recule en vacillant puis bascule par-dessus les
remparts, tombant parmi les combattants engagés dans la
bataille qui fait rage. Sa monture emplumée s'envole en poussant
un hideux croassement dans le ciel d'orage. Vous trouvez alors
sur le sol taché de sang un magnifique Médaillon d'Onyx arraché
à l'armure du Guerrier au moment de sa chute. Si vous souhaitez
conserver ce Médaillon d'Onyx, glissez-le dans votre poche et
inscrivez-le sur votre Feuille d'Aventure dans la case Objets
Spéciaux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("MÉDAILLON D'ONYX", key="medaillon", label="Prendre le Médaillon d'Onyx")

    st.write_stream(stream_text("Quittez à présent la tour de guet en vous rendant au :"))
    st.page_link("tomes/tome4/page_59.py", label="59", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
