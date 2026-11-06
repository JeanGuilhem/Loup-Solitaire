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

check_inventory(current_page_number=314, book=6)

fr_text = """
Le pirate lance son couteau qui se dirige en sifflant vers votre
poitrine. Vous suivez des yeux la lame brillante puis, anticipant
sa trajectoire, vous vous élancez vers elle, et à la seconde même
où elle va vous atteindre, vous faites un bond sur le côté pour
l'éviter. Complètement déconcerté par ce qu'il vient de voir, le
pirate est incapable de réagir à votre attaque et avant qu'il ait
compris ce qui lui arrive, il est précipité dans les eaux noires de
la Storn.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
