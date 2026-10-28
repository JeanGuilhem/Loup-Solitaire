import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=197, book=3)

fr_text = """
Vous apercevez un autre passage qui permet de quitter la caverne
en prenant la direction du nord.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez passer sans bruit devant les créatures endormies pour atteindre ce tunnel, rendez-vous au :'))
    st.page_link("tomes/tome3/page_125.py", label="125", icon="📄")
    st.write_stream(stream_text("Si vous préférez ne pas prendre le risque de les réveiller, vous pouvez retourner sur vos pas et emprunter l'autre tunnel en vous rendant au :"))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")
    st.write_stream(stream_text('Enfin, si vous désirez attaquer les créatures endormies, vous pouvez le faire en vous rendant au :'))
    st.page_link("tomes/tome3/page_109.py", label="109", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
