import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=76, book=2)

fr_text = """
En fouillant ses longs vêtements tachés de sang, vous vous rendez
compte avec un sentiment de malaise qu'aucune preuve ne permet
d'affirmer que cet homme était bien celui qui cherchait à vous tuer.
Vous ne trouvez sur lui qu'un Poignard et 2 Pièces d'Or que vous
pouvez vous approprier si vous le désirez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
    pickup_gold(2)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
