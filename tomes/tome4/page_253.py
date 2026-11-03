import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=253, book=4)

fr_text = """
Vous vous apprêtez à donner l'ordre à vos hommes de dresser le
camp, lorsqu'un éclaireur en provenance de l'est apparaît
soudain, galopant vers vous. Il vous montre alors une rangée de
cavaliers dont les silhouettes se dessinent à l'horizon. « Des
brigands ! » s'écrie-t-il. Vous estimez leur nombre à 200 au
moins. Les brigands chevauchent dans votre direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous avez atteint le rang Kaï de Guerrier (ce qui signifie que vous maîtrisez huit Disciplines), rendez-vous au :'))
    if kai_rank() >= 8:
        st.page_link("tomes/tome4/page_72.py", label="72", icon="📄")
    else:
        st.write_stream(stream_text("Vous n'avez pas atteint le rang Kaï de Guerrier."))
        st.page_link("tomes/tome4/page_72.py", label="72", icon="📄", disabled=True)
    st.write_stream(stream_text('Dans le cas contraire, rendez-vous au :'))
    st.page_link("tomes/tome4/page_135.py", label="135", icon="📄", disabled=kai_rank() >= 8)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
