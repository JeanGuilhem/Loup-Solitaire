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

check_inventory(current_page_number=33, book=5)

fr_text = """
En balayant de la main l'épaisse couche de poussière qui
recouvre le sol, vous découvrez un gros anneau de métal qui
semble scellé dans une vieille trappe. Le métal est usé par la
rouille, mais vous réussissez cependant à soulever la trappe.
Celle-ci s'ouvre sur un puits profond d'où s'échappent les relents
nauséabonds des égouts. Les Sharnazims sont maintenant en
train de monter les marches en pierre, et leurs pas lourds font
écho aux battements précipités de votre cœur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez sauter dans le puits, rendez-vous au :'))
    st.page_link("tomes/tome5/page_94.py", label="94", icon="📄")
    st.write_stream(stream_text('Si vous préférez vous redresser pour affronter les Sharnazims, rendez-vous au :'))
    st.page_link("tomes/tome5/page_185.py", label="185", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
